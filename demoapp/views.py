import re
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Employeedetails,Employeeuploadfile
from django.contrib.auth.models import User
from .forms import EmployeedetailsForm,EmployeeuploadfileForm
from django.core.files.storage import FileSystemStorage



class EmployeeDeatils(TemplateView):

    def get(self,request):
        print(request,'=============req')
        form = EmployeedetailsForm()
        query_obj = Employeedetails.objects.values() #
        print(query_obj,'=========query_obj')
        return render(request,'demoapp.html',{'query_obj':query_obj,"form":form})

    def post(self,request):
        

        form = EmployeedetailsForm(request.POST)
        fname  = request.POST.get('fname')
        lname  = request.POST.get('lname')
        designation  = request.POST.get('designation')
        
        user = request.POST.get('user')
        print(fname,'=======fname')
        print(user,'============user')

        if  request.POST.get('active') == 'on':
            active  = True
        else:
            active = False

        print(active,'====active')

        userdetail = User.objects.get(id=request.POST.get('user'))
        print(userdetail,'===========userdetail')

        query_save = Employeedetails.objects.create(user=userdetail,fname=fname,lname=lname,designation=designation,active=active)
        query_save.save()

        query_obj = Employeedetails.objects.values()

        form = EmployeedetailsForm()

        return render(request,'demoapp.html',{'query_obj':query_obj,'form':form})#




class EmployeedetailsFormsubmit(TemplateView):
    def get(self,request):
        form = EmployeeuploadfileForm()
        return render(request,'EmployeedetailsForm.html',{'form':form})
    def post(self,request):
        
        form = EmployeeuploadfileForm(request.POST, request.FILES)
        print(request.FILES,'-----------------------------')

        if form.is_valid():
            emp = request.POST.get('emp')

            newdoc =request.FILES['upload_file']

            description = request.POST.get('description')

            print(emp,newdoc,description)
            form.save()
        else:
            print('no')

        return render(request,'EmployeedetailsForm.html')
