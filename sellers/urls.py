from django.urls import path
from .views import sell_item


urlpatterns=[
     path('sell/',sell_item,name='sell_item'),
   
]
