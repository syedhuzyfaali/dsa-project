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
    path('student/view_test_results', Student.view_test_results, name='student_view_test_results'),
    path('student/view_class_schedule', Student.view_class_schedule, name='student_view_class_schedule'),
    path('student/view_grade_history', Student.view_grade_history, name='student_view_grade_history'),
]

teacher_urls = [
    path('teacher/dashboard', Teacher.dashboard, name='teacher_dashboard'),
    path('teacher/profile', Teacher.profile, name='teacher_profile'),
    path('teacher/courses', Teacher.courses, name='teacher_courses'),
]

admin_urls = [
    path('admin/dashboard', Admin.dashboard, name='admin_dashboard'),
    path('admin/dashboard/admission', Admin.dashboard_admission, name='admin_dashboard_admission'),
    path('admin/dashboard/courses_creation', Admin.dashboard_courses_creation, name='admin_dashboard_courses_creation'),
    path('admin/profile', Admin.profile, name='admin_profile'),
    path('admin/courses', Admin.courses, name='admin_courses'),
    path('admin/admission/add_student', Admin.add_student, name='admin_add_student'),
    path('admin/admission/add_teacher', Admin.add_teacher, name='admin_add_teacher'),
    path('admin/admission/add_admin', Admin.add_admin, name='admin_add_teacher'),
    path('admin/create_course', Admin.create_course, name='admin_create_course'),
    path('admin/create_class', Admin.create_class, name='admin_create_class'),
    path('admin/create_semester', Admin.create_semester, name='admin_create_semester'),
]

urlpatterns += student_urls
urlpatterns += teacher_urls
urlpatterns += admin_urls