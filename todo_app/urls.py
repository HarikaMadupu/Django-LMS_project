from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('delete/<int:pk>/', views.delete_task, name='delete'),
    path('complete/<int:pk>/', views.complete_task, name='complete'),
]



