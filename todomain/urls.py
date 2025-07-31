from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.Home,name='index'),
    path('add/',views.Add,name='add'),
    path('done/<int:id>/',views.Done,name='done'),
    path('delete/<int:id>/',views.Delete,name='delete'),
    path('edit/<int:id>/',views.Edit,name='edit'),
    path('undone/<int:id>/',views.Undone,name='undone'),
]