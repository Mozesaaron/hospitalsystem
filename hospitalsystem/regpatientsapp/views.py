from django.shortcuts import render
from regpatientsapp.models import *

# Create your views here.

def regpatients(request):
    return render(request , "regpatients.html")

def appointments(request):
    patients = Patients.objects.all()
    return render(request , 'appointments.html' , {'patients':patients})

def patientsonboard(request):
    patients = Patients.objects.all()
    return render(request ,  'patientsonboard.html' , {'patientsonboard':patients})

def prescribe(request):
    patients = Patients.objects.all()
    return render(request , "prescribe.html" , {'patients':patients})

def chat(request):
    patients = Patients.objects.all()
    return render(request , "chat.html" , {'patients':patients})

def checkonpatients(request):
    patients = Patients.objects.all()
    return render(request , 'checkonpatients.html' , {'patients':patients})

def regpat(request):
    if request.method == 'POST':
        patientnames = request.POST.get('names')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        patientssituation = request.POST.get('patientssituation')
        healthissues  = request.POST.get('healthissues')
        dateregistered = request.POST.get('dateregistered')

        patients_instance = Patients(
            names = patientnames ,
            gender = gender ,
            age = age ,
            patientssituation = patientssituation ,
            healthissues = healthissues ,
            dateregistered = dateregistered
        )

        patients_instance.save()
        return render(request , "regpatients.html" , {'registered':'Patient Registered'})



















