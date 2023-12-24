from django.urls import path
from . import views


urlpatterns=[
    path('myauction',views.myauction, name='myauction'),
    ]
