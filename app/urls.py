from .views import *
from django.urls import path


urlpatterns = [
    path('', hero, name='index'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    
] 

student_urls = [
    path('student/dashboard', StudentView.dashboard, name='student_dashboard'),
    path('student/profile', StudentView.profile, name='student_profile'),
    path('student/courses', StudentView.courses, name='student_courses'),
    path('student/view_test_results', StudentView.view_test_results, name='student_view_test_results'),
    path('student/view_class_schedule', StudentView.view_class_schedule, name='student_view_class_schedule'),
    path('student/view_grade_history', StudentView.view_grade_history, name='student_view_grade_history'),
]

teacher_urls = [
    path('teacher/dashboard', TeacherView.dashboard, name='teacher_dashboard'),
    path('teacher/profile/<int:instructor_id>', TeacherView.profile_view, name='teacher_profile'),
    path('teacher/courses', TeacherView.courses, name='teacher_courses'),
    path('teacher/class_schedule', TeacherView.teacher_class_schedule, name='teacher_class_schedule'),
]

admin_urls = [
    path('admin/dashboard', AdminView.dashboard, name='admin_dashboard'),
    path('admin/dashboard/admission', AdminView.dashboard_admission, name='admin_dashboard_admission'),
    path('admin/dashboard/courses_creation', AdminView.dashboard_courses_creation, name='admin_dashboard_courses_creation'),
    path('admin/profile/', AdminView.profile, name='admin_profile'),
    path('admin/courses', AdminView.courses, name='admin_courses'),
    path('admin/admission/add_student', AdminView.add_student, name='admin_add_student'),
    path('admin/admission/add_teacher', AdminView.add_teacher, name='admin_add_teacher'),
    path('admin/admission/add_admin', AdminView.add_admin, name='admin_add_admin'),
    path('admin/create_course', AdminView.create_course, name='admin_create_course'),
    path('admin/create_class', AdminView.create_class, name='admin_create_class'),
    path('admin/create_semester', AdminView.create_semester, name='admin_create_semester'),
    path('admin/create_course_enrollment', AdminView.create_course_enrollment, name='admin_create_course_enrollment'),
]


urlpatterns += student_urls
urlpatterns += teacher_urls
urlpatterns += admin_urls