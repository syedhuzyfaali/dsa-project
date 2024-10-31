from .views import *
from django.urls import path


urlpatterns = [
    path('', hero, name='index'),
    path('login', login, name='login'),
    path('dashboard', Student.dashboard, name='dashboard'),

]