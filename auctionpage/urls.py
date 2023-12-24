from django.urls import path
from . import views
from .views import productdetails

app_name = 'myapp'
urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('sell', views.sell,name='sell'),
    path('productdetails/<int:id>/',productdetails, name='productdetails'),
]