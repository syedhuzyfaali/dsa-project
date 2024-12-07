from django.shortcuts import render

# Create your views here.
def hero(request):
    return render(request, 'initial/Hero.html')

def login(request):
    return render(request, 'initial/Login.html')

def logout(request):
        return render(request, 'initial/Login.html')

class Student:
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
    
class Admin:
    def dashboard(request):
        return render(request, 'admin_panel/Dashboard.html')

    def profile(request):
        return render(request, 'admin_panel/Profile.html')
    
    def courses(request):
        return render(request, 'Courses.html')
    
    def add_student(request):
        return render(request, 'admin_panel/Add_Student_Page.html')
    
    def add_teacher(request):
        return render(request, 'admin_panel/Add_Teacher_Page.html')
   
    def add_admin(request):
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

class Teacher:
    def dashboard(request):
        return render(request, 'teacher/Dashboard.html')

    def profile(request):
        return render(request, 'teacher/Profile.html')
    
    def courses(request):
        return render(request, 'Courses.html')