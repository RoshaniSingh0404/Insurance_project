from django.urls import path,re_path
from django.conf.urls.static import static
from django.conf import settings
from demoapp.views import  *
from . import views
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    re_path('^emp',EmployeeDeatils.as_view(),name='EmployeeDeatils'),
    re_path('^EmployeedetailsFormsubmit',EmployeedetailsFormsubmit.as_view(),name='EmployeedetailsFormsubmit')





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

