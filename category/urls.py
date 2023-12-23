from django.urls import path
from .views import product_list

urlpatterns=[
    path('products/<str:category>/', product_list, name='product_list')
]

