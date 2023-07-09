from .models import Employeedetails
from django import forms



class EmployeedetailsForm(forms.ModelForm):
    
    class Meta:
        model = Employeedetails
        fields = ("user","fname","lname","designation","active")
