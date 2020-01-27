from django.urls import path
from . import views
urlpatterns = [
    path('adduserr/',views.add_userr,name="add_userr"),
    path('',views.view_userr, name="view_userr"),
    path('edit-userr/<int:pid>/',views.edit_userr,name="edit_userr"),
    path('delete-userr/<int:pid>/',views.delete_userr,name="delete_userr"),
    path('add1/',views.add_new_userr, name="add_userr"),
]