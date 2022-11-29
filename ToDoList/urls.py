from django.urls import path

from . import views

urlpatterns = [
    path('task/', views.task_list.as_view()),
    path('task/<int:pk>/', views.task_detail.as_view()),
    path('task/put/<int:pk>/', views.task_put.as_view()),
    path('task/delete/<int:pk>/', views.task_delete.as_view()),
]