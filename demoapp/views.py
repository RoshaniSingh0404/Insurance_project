from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from .models import Employee



class EmployeeDeatils(TemplateView):
    def get(self,request):
        return render(request,'demoapp.html')
    def post(self,request):
        return render(request,'demoapp.html')