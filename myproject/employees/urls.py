from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('LoginForm',views.Login)
]