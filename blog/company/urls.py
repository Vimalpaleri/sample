from django.urls import path
from . import views
urlpatterns = [
    path('employee-reg/',views.add_empolyee,name="empolyee-reg"),
    path('employee-login/',views.login_employee,name="empolyee-login"),
    path('employee-dashboard/',views.dashboard,name="dashboard"),
    path('employee-logout/',views.emp_logout,name="emp-logout"),
    path('upload',views.upload),
    path('mupload',views.mupload),
]




