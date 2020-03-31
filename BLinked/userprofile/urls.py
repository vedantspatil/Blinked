from django.urls import path

from . import views

urlpatterns = [
    path('<str:username>/', views.index, name='index'),
    path('edit/education/new', views.addEducation, name='addEducation'),
    path('edit/topcard', views.editDetails, name='editDetails'),
]

