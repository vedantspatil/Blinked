from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:jobId>/', views.job, name='job'),
]

