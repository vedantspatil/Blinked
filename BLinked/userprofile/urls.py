from django.urls import path

from . import views

urlpatterns = [
    path('<str:username>/', views.index, name='index'),
    path('settings/edit/', views.edit, name='edit'),
]

