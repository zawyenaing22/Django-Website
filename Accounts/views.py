from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return render(request,'Accounts/dashboard.html')

def customers(request):
    return render(request,'Accounts/customers.html')

def products(request):
    return render(request,'Accounts/products.html')
