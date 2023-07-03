from ast import Delete
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# CASCADE : If parent is Delete than child will also be deleted
# SET_NULL :  If parent is Delete than child will not be deleted
# auto_now : Creates datefield data automatically can't be changed
# auto_now_add : Can be updated
# python manage.py shell : To interact with shell, Can write queries and modify

class Employeedetails(models.Model):
    user = models.ForeignKey(User,unique=True,on_delete=models.CASCADE)
    fname = models.CharField(max_length=50,null=True,blank=True)
    lname = models.CharField(max_length=50,null=True,blank=True)
    designation = models.CharField(max_length=50,null=True,blank=True)
    active = models.BooleanField(default=True)
    joined_on = models.DateField(auto_now=True)
    update_on = models.DateField(auto_now_add=True,null=True,blank=True)

    

    def __str__(self):
        return ("{}/{}---{}".format(self.fname,self.lname,self.designation))

