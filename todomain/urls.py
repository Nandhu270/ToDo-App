from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.Home,name='index'),
    path('add/',views.Add,name='add')
]