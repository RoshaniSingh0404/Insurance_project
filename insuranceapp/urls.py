from django.urls import path,re_path
from django.conf.urls.static import static
from django.conf import settings
from insuranceapp.views import  *
from . import views





urlpatterns = [
    re_path('loginpage',loginpage.as_view(),name='loginpage'),
    re_path('login/', views.login_view, name='login'),
    re_path('registerationpage',registerationpage.as_view(),name='registerationpage'),
    re_path('somepage',somepage.as_view(),name='somepage'),
    re_path('EmployeeBasedView',EmployeeBasedView.as_view(),name='EmployeeBasedView'),

    re_path('^EmployeeDeatils',EmployeeDeatils.as_view(),name='EmployeeDeatils'),


]
