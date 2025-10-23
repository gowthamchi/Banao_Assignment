from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Patient, Doctor

def hello(request):
    return HttpResponse("Hello world from myapp")

def hello1(request):
    return render(request, 'hello.html')

def doctorsignup(request):
    return render(request, 'doctor_signup.html')

def patientsignup(request):
    return render(request, 'patient_signup.html')

def patient_signup(request):
    if request.method == 'POST':
        try:
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address = request.POST.get('address')
            profile_pic = request.FILES.get('photo')

            print(f"Received data: {first_name}, {last_name}, {username}, {email}")

            patient = Patient.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
                address=address,
                profile_picture=profile_pic
            )

            context = {
                'username': patient.username,
                'email': patient.email,
                'first_name': patient.first_name,
                'last_name': patient.last_name
            }

            print(f"Context: {context}")

            return render(request, 'patient_dashboard.html', context)
        
        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse(f"Error occurred: {e}")

    return render(request, 'patient_signup.html')

def doctor_signup(request):
    if request.method == 'POST':
        try:
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address = request.POST.get('address')
            profile_pic = request.FILES.get('photo')

            print(f"Received data: {first_name}, {last_name}, {username}, {email}")

            doctor = Doctor.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
                address=address,
                profile_picture=profile_pic
            )

            context = {
                'username': doctor.username,
                'email': doctor.email,
                'first_name': doctor.first_name,
                'last_name': doctor.last_name
            }

            print(f"Context: {context}")

            return render(request, 'doctor_dashboard.html', context)
        
        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse(f"Error occurred: {e}")

    return render(request, 'doctor_signup.html')

def patient_logout(request):
    return redirect('patient_signup_page')

def doctor_logout(request):
    return redirect('doctor_signup_page')