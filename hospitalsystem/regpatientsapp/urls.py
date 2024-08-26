from django.contrib import admin
from django.urls import path
from regpatientsapp import views
from django.urls import path, include

urlpatterns = [
    path('regpatient' , views.regpatients , name='regpatient' ),
    path('appointments' , views.appointments , name='appointment' ),
    path('patientsonboard' , views.patientsonboard , name = 'patientsonboard'),
    path('prescribe' , views.prescribe , name = 'prescribe'),
    path('chatroom' , views.chat , name = 'chat'),
    path('checkonpatients' , views.checkonpatients , name = 'checkonpatients'),

    path('regpat' , views.regpat , name='regpat'),
]