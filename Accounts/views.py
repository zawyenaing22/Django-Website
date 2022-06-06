from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("Dashboard Page")

def about(request):
    return HttpResponse("About Page")

def contacts(request):
    return HttpResponse("Contacts Page")
