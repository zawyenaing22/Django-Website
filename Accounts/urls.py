from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def dashboard(request):
    return HttpResponse("Dashboard Page")

def about(request):
    return HttpResponse("About Page")

def contacts(request):
    return HttpResponse("Contacts Page")

urlpatterns = [
    path('',dashboard),
    path('about/',about),
    path('contacts',contacts),
]