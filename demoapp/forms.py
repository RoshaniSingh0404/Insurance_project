from .models import Employeedetails,Employeeuploadfile
from django import forms



class EmployeedetailsForm(forms.ModelForm):
    
    class Meta:
        model = Employeedetails
        fields = ("user","fname","lname","designation","active")


class EmployeeuploadfileForm(forms.ModelForm):
    
    class Meta:
        model = Employeeuploadfile
        fields = ("emp","upload_file","description")

