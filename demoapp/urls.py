from django.urls import path,re_path
from django.conf.urls.static import static
from django.conf import settings
from demoapp.views import  *
from . import views





urlpatterns = [
    re_path('^EmployeeDeatils',EmployeeDeatils.as_view(),name='EmployeeDeatils'),



]
