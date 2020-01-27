from django.urls import path
from . import views
urlpatterns = [
    path('addproduct/',views.add_product,name="add_product"),
    path('products',views.view_products, name="view_products"),
    path('edit-products1/<int:pid>/',views.edit_product,name="edit_products"),
    path('delete-products1/<int:pid>/',views.delete_product,name="delete_products"),

]