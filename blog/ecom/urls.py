from django.urls import path
from . import views
urlpatterns = [
    path('addcat/',views.add_category,name="add_cat"),
    path('addprod/',views.add_product),
    path('show/',views.mainEcom),
    path('showprod/<int:pid>/',views.viewProd,name="view_prod"),

    # path('edit-products1/<int:pid>/',views.edit_product,name="edit_products"),
    # path('delete-products1/<int:pid>/',views.delete_product,name="delete_products"),

]