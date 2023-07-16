from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm,EmployeeForm
from .models import Employee




# Create your views here.

class registerationpage(TemplateView):
    def get(self,request):
        form = UserCreationForm()
        return render(request,'register_page.html',{'form':form})

    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('loginpage')

        else:
            return render(request,'register_page.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('somepage')  # Replace 'home' with your desired homepage URL
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'login_page.html', {'form': form})


class loginpage(TemplateView):
    def get(self,request):
        form = LoginForm()
        return render(request,'login_page.html', {'form': form})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
        
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('somepage')  # Replace 'home' with your desired homepage URL
            else:
                form.add_error(None, 'Invalid username or password.')
                return render(request,'login_page.html')
        else:
            return render(request,'login_page.html')

class somepage(TemplateView):
    def get(self,request):

        return render(request,'somepage.html')
    def post(self,request):
        return render(request,'somepage.html')


class EmployeeBasedView(TemplateView):
    def get(self,request):
        form = EmployeeForm()
        return render(request,'employeeform.html',{'form':form})

    def post(self,request):
        form = EmployeeForm(request.POST)
        fname = request.POST.get("first_name") 
        lname = request.POST.get("last_name") 
        emp_id = request.POST.get("emp_id") 

        print(fname,lname,emp_id,'==========')

        ###method1

        # Employee.objects.create(first_name=fname,last_name=lname,emp_id=emp_id)

        ###method2
        
        if form.is_valid():
            form.save()
            print("succcessfully done")
            return redirect('somepage')
        else:
            
            print('noooooooooo')
            form.error()
        return render(request,'employeeform.html')


class EmployeeDeatils(TemplateView):
    def get(self,request):
        return render(request,'base.html')
    def post(self,request):
        return render(request,'base.html')





