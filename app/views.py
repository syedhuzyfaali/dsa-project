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
        return render(request, 'Profile.html')
    
    def courses(request):
        return render(request, 'Courses.html')
    
class Admin:
    def dashboard(request):
        return render(request, '/Dashboard.html')

    def profile(request):
        return render(request, 'Profile.html')
    
    def courses(request):
        return render(request, 'Courses.html')

class Teacher:
    def dashboard(request):
        return render(request, '/Dashboard.html')

    def profile(request):
        return render(request, 'Profile.html')
    
    def courses(request):
        return render(request, 'Courses.html')