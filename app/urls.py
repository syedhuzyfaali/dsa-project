from .views import *
from django.urls import path


urlpatterns = [
    path('', hero, name='index'),
    path('login', login, name='login'),
    
] 

student_urls = [
    path('student/dashboard', Student.dashboard, name='student_dashboard'),
    path('student/profile', Student.profile, name='student_profile'),
    path('student/courses', Student.courses, name='student_courses'),
]

teacher_urls = [
    path('teacher/dashboard', Teacher.dashboard, name='teacher_dashboard'),
    path('teacher/profile', Teacher.profile, name='teacher_profile'),
    path('teacher/courses', Teacher.courses, name='teacher_courses'),
]

admin_urls = [
    path('admin/dashboard', Admin.dashboard, name='admin_dashboard'),
    path('admin/profile', Admin.profile, name='admin_profile'),
    path('admin/courses', Admin.courses, name='admin_courses'),
]

urlpatterns += student_urls
urlpatterns += teacher_urls
urlpatterns += admin_urls