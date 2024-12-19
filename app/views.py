from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admin,Student,Instructor

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
            request.session['user_id'] = admin.id
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
        return render(request, 'student/Profile.html')
    
    def courses(request):
        return render(request, 'Courses.html')
    
    def view_test_results(request):
        return render(request, 'student/Student Test Result.html')
    
    def view_grade_history(request):
        return render(request, 'student/Student Grade History.html')
    
    def view_class_schedule(request):
        return render(request, 'student/Student Class Schedule.html')

# Rename Admin to AdminView
class AdminView:
    def dashboard(request):
        return render(request, 'admin_panel/Dashboard.html')

    def profile(request):
        return render(request, 'admin_panel/Profile.html')
    
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
        return render(request, 'admin_panel/Create_Course.html')
    
    def create_course_enrollment(request):
        return render(request, 'admin_panel/Create_Course_Enrollment.html')

    def create_class(request):
        return render(request, 'admin_panel/Create_Class.html')

    def create_semester(request):
        return render(request, 'admin_panel/Create_Semester.html')

class TeacherView:
    def dashboard(request):
        return render(request, 'teacher/Dashboard.html')

    def profile(request):
        return render(request, 'teacher/Profile.html')
    
    def courses(request):
        return render(request, 'Courses.html')
