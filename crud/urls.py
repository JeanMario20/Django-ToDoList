from django.urls import path
from . import views

urlpatterns  = [
    path('list/add_task', views.add_taks, name='list'),
    path('list/', views.list, name="list"),
    path('edit-task/<str:pk>', views.editTask, name="edit-task"),
    path('delete-task/<str:pk>' , views.deleteTask, name="delete-task"),
]