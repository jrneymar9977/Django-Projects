from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('sell', views.sell,name='sell')
]