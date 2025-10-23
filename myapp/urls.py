from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello1, name='home'),
    path('doctorsignup/', views.doctorsignup, name='doctor_signup_page'),
    path('patientsignup/', views.patientsignup, name='patient_signup_page'),
    path('patientdashboard/', views.patient_signup, name='patient_dashboard'),
    path('doctordashboard/', views.doctor_signup, name='doctor_dashboard'),
    path('patientlogout/', views.patient_logout, name='patient_logout'),
    path('doctorlogout/', views.doctor_logout, name='doctor_logout'),
]