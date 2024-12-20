from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admin,Student,Instructor,Semester,Course,Class,Enrollment
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.
def hero(request):
    return render(request, 'initial/Hero.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        admin = Admin.objects.filter(email=email).first()
        if admin and admin.password == password:
            request.session['user_type'] = 'admin'
            request.session['admin_id'] = admin.id
            request.session['user_name'] = admin.full_name
            messages.success(request, 'Admin logged in successfully!')
            return redirect('admin_dashboard')

        student = Student.objects.filter(email=email).first()
        if student and student.password == password:
            request.session['user_type'] = 'student'
            request.session['user_id'] = student.id
            request.session['user_name'] = student.full_name
            messages.success(request, 'Student logged in successfully!')
            return redirect('student_dashboard')

        instructor = Instructor.objects.filter(email=email).first()
        if instructor and instructor.password == password:
            request.session['user_type'] = 'instructor'
            request.session['user_id'] = instructor.id
            request.session['user_name'] = instructor.name
            messages.success(request, 'Instructor logged in successfully!')
            return redirect('teacher_dashboard')

        messages.error(request, 'Invalid credentials. Please try again.')
        return redirect('login')

    return render(request, 'initial/Login.html')

def logout(request):
    request.session.flush()  
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login') 

def dashboard(request):
    
    user_type = request.session.get('user_type')
    if user_type == 'admin':
        return render(request, 'admin_panel/Dashboard.html')
    elif user_type == 'student':
        return render(request, 'student/Dashboard.html')
    elif user_type == 'instructor':
        return render(request, 'teacher/Dashboard.html')
    else:
        return redirect('login') 

class StudentView:
    def dashboard(request):
        return render(request, 'student/Dashboard.html')

    def profile(request):

        user_id = request.session.get('user_id')
        student = Student.objects.get(id=user_id)
        
        return render(request, 'student/Profile.html', {'student': student})
    
    def courses(request):
        return render(request, 'Courses.html')
    
    def view_test_results(request):
        return render(request, 'student/Student Test Result.html')
    
    def view_grade_history(request):
        return render(request, 'student/Student Grade History.html')
    
    def view_class_schedule(request):
        user_id = request.session.get('user_id')
        
        # Ensure that the user is logged in
        if not user_id:
            return redirect('login')
        
        # Get the student object
        student = Student.objects.get(id=user_id)

        # Get the courses that the student is enrolled in
        enrollments = Enrollment.objects.filter(student=student)
        
        # Prepare a list to pass to the template
        schedule = []
        for enrollment in enrollments:
            course_class = enrollment.course_class
            schedule.append({
                'class_id': course_class.id,
                'course_name': course_class.course.name,
                'teacher': course_class.instructor.name,
                'time_slot': course_class.time_slot,
                'day': course_class.day_of_week,
                'semester': f"{course_class.semester.type} - {course_class.semester.year}",
            })
        
        return render(request, 'student/Student Class Schedule.html', {'schedule': schedule})
    
    def view_fee_bill(request):
        user_id = request.session.get('user_id')

        if not user_id:
            return redirect('login')

        # Get the student's details
        student = Student.objects.filter(id=user_id).first()

        if not student:
            messages.error(request, "Student not found!")
            return redirect('login')

        # Get the student's enrolled classes and calculate total fees
        enrollments = Enrollment.objects.filter(student_id=user_id)
        total_fees = sum(
            enrollment.course_class.course.credit_hr * enrollment.course_class.semester.fees_per_credit_hour
            for enrollment in enrollments
        )

        # Pass semesters and enrollment data to the template
        semesters = Semester.objects.all()
        fee_data = [
            {
                "class_id": enrollment.course_class.id,
                "course_name": enrollment.course_class.course.name,
                "fees": enrollment.course_class.course.credit_hr * enrollment.course_class.semester.fees_per_credit_hour,
            }
            for enrollment in enrollments
        ]

        return render(request, 'student/FeeBill.html', {
            "semesters": semesters,
            "fee_data": fee_data,
            "total_fees": total_fees,
            "student_info": {
                "name": student.full_name,
                "father_name": student.father_name,
                "email": student.email,
            }
        })


class AdminView:
    def dashboard(request):
        return render(request, 'admin_panel/Dashboard.html')

    def profile(request):
        admin_id = request.session.get('admin_id')
        if not admin_id:
            return redirect('login')  # Redirect if admin_id is not available

        admin = get_object_or_404(Admin, id=admin_id)
        return render(request, 'admin_panel/Profile.html', {'admin': admin})
    
    def courses(request):
        return render(request, 'Courses.html')
    
    def add_student(request):
        if request.method == 'POST':
            full_name = request.POST.get('full_name')
            father_name = request.POST.get('father_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            date_of_birth = request.POST.get('date_of_birth')
            date_of_enrollment = request.POST.get('date_of_enrollment')

            if not all([full_name, father_name, email, password, date_of_birth, date_of_enrollment]):
                messages.error(request, 'All fields are required.')
                return redirect('admin_add_student')

            if Student.objects.filter(email=email).exists():
                messages.error(request, 'A student with this email already exists.')
                return redirect('admin_add_student')

            Student.objects.create(
                full_name=full_name,
                father_name=father_name,
                email=email,
                password=password,
                date_of_birth=date_of_birth,
                date_of_enrollment=date_of_enrollment
            )
            messages.success(request, 'Student added successfully!')
            return redirect('admin_dashboard')

        return render(request, 'admin_panel/Add_Student_Page.html')

    def add_teacher(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            hiring_date = request.POST.get('hiring_date')
            expertise = request.POST.get('expertise')

            if not all([name, email, password, hiring_date, expertise]):
                messages.error(request, 'All fields are required.')
                return redirect('admin_add_teacher')

            if Instructor.objects.filter(email=email).exists():
                messages.error(request, 'An instructor with this email already exists.')
                return redirect('admin_add_teacher')

            instructor = Instructor(
                name=name,
                email=email,
                password=password,  
                hiring_date=hiring_date,
                expertise=expertise
            )
            instructor.save()

            messages.success(request, 'Instructor added successfully!')
            return redirect('admin_dashboard')  

        return render(request, 'admin_panel/Add_Teacher_Page.html')


    def add_admin(request):
        if request.method == 'POST':
            full_name = request.POST.get('full_name')  
            email = request.POST.get('email')         
            password = request.POST.get('password')   

            if not full_name or not email or not password:
                messages.error(request, 'All fields are required.')
                return redirect('admin_add_admin')

            if Admin.objects.filter(email=email).exists():
                messages.error(request, 'An admin with this email already exists.')
                return redirect('admin_add_admin')

            Admin.objects.create(full_name=full_name, email=email, password=password)
            messages.success(request, 'Admin added successfully!')
            return redirect('admin_dashboard')  

        return render(request, 'admin_panel/Add_Admin_Page.html')
    
    def dashboard_admission(request):
        return render(request, 'admin_panel/Dashboard Admission.html') 
    
    def dashboard_courses_creation(request):
        return render(request, 'admin_panel/Dashboard Course Creation.html')
    
    def create_course(request):
        if request.method == 'POST':
            course_name = request.POST.get('course_name')
            course_detail = request.POST.get('course_detail')
            course_credit_hr = request.POST.get('course_credit_hr')

            if not all([course_name, course_detail, course_credit_hr]):
                messages.error(request, 'All fields are required.')
                return redirect('create_course')

            try:
                Course.objects.create(
                    name=course_name,
                    detail=course_detail,
                    credit_hr=int(course_credit_hr)
                )
                messages.success(request, 'Course created successfully!')
                return redirect('admin_dashboard')
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
                return redirect('create_course')

        return render(request, 'admin_panel/Create_Course.html')

    def create_course_enrollment(request):
        if request.method == 'POST':
            student_id = request.POST.get('StudentId')
            class_id = request.POST.get('class_id')

            course_class = get_object_or_404(Class, id=class_id)

            try:
                student = Student.objects.get(id=student_id)
            except Student.DoesNotExist:
                messages.error(request, f'Student with ID {student_id} does not exist.')
                return redirect('admin_dashboard') 
            existing_enrollment = Enrollment.objects.filter(student=student, course_class=course_class).exists()

            if existing_enrollment:
                messages.error(request, f'{student.full_name} is already enrolled in {course_class.course.name}.')
            else:
                Enrollment.objects.create(student=student, course_class=course_class)
                messages.success(request, f'Student {student.full_name} has been enrolled in {course_class.course.name}.')

            return redirect('admin_dashboard')  

        classes = Class.objects.all()
        return render(request, 'admin_panel/Create_Course_Enrollment.html', {'classes': classes})

    def create_class(request):
        if request.method == "POST":
            course_id = request.POST.get('course')
            teacher_id = request.POST.get('teacher')
            semester_id = request.POST.get('semester')
            room_name = request.POST.get('room')
            day_of_week = request.POST.get('day')
            time_slot = request.POST.get('time_slot')

            course = Course.objects.get(id=course_id)
            instructor = Instructor.objects.get(id=teacher_id)
            semester = Semester.objects.get(id=semester_id)

            Class.objects.create(
                course=course,
                instructor=instructor,
                semester=semester,
                room_name=room_name,
                day_of_week=day_of_week,
                time_slot=time_slot
            )
            messages.success(request, "Class created successfully!")
            return redirect('admin_dashboard')

        courses = Course.objects.all()
        instructors = Instructor.objects.all()
        semesters = Semester.objects.all()
        return render(request, 'admin_panel/create_class.html', {
            'courses': courses,
            'teachers': instructors,
            'semesters': semesters
        })

    def create_semester(request):
        if request.method == 'POST':
            semester_type = request.POST.get('type')
            year = request.POST.get('year')
            fees_per_credit_hour = request.POST.get('fees')

            # Validation for inputs
            if not semester_type or not year or not fees_per_credit_hour:
                messages.error(request, 'All fields are required.')
                return redirect('create_semester')

            # Create the semester record
            Semester.objects.create(
                type=semester_type,
                year=year,
                fees_per_credit_hour=fees_per_credit_hour
            )
            messages.success(request, 'Semester created successfully!')
            return redirect('admin_dashboard')

        return render(request, 'admin_panel/Create_Semester.html')

class TeacherView:
    def dashboard(request):
        user_id = request.session.get('user_id')
        instructor = Instructor.objects.get(id=user_id)
        return render(request, 'teacher/Dashboard.html', {'instructor': instructor})

    def profile_view(request, instructor_id):
        instructor = get_object_or_404(Instructor, id=instructor_id)

        if instructor.expertise:
            expertise_list = instructor.expertise.split(',')
            expertise_str = ", ".join(expertise_list)
        else:
            expertise_str = "No expertise listed"

        return render(request, 'teacher/Profile.html', {'instructor': instructor, 'expertise_str': expertise_str})

    def teacher_class_schedule(request):
        user_id = request.session.get('user_id')
        
        # Ensure that the user is logged in
        if not user_id:
            return redirect('login')
        
        # Get the instructor object
        instructor = Instructor.objects.get(id=user_id)
        
        # Get the classes that the instructor is teaching
        classes = Class.objects.filter(instructor=instructor)
        
        # Prepare a list to pass to the template
        schedule = []
        for course_class in classes:
            schedule.append({
                'class_id': course_class.id,
                'course_name': course_class.course.name,
                'time_slot': course_class.time_slot,
                'day': course_class.day_of_week,
                'semester': f"{course_class.semester.type} - {course_class.semester.year}",
            })
        
        # Pass instructor information to the template
        return render(request, 'teacher/teacher_class_schedule.html', {'schedule': schedule, 'instructor': instructor})
    
    def courses(request):
        return render(request, 'Courses.html')
