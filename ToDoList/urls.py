from django.urls import path

from . import views

urlpatterns = [
    path('task/', views.task_list.as_view(), name="task"),
    path('task/add/', views.task_post.as_view(), name="task_post"),
    path('task/complete/', views.task_list_complete.as_view(), name="task_list_complete"),
    path('task/uncomplete/', views.task_list_uncomplete.as_view(), name="task_list_uncomplete"),
    path('task/<int:pk>/', views.task_detail.as_view(), name="task_detail"),
    path('task/put/<int:pk>/', views.task_put.as_view(), name="task_update"),
    path('task/delete/<int:pk>/', views.task_delete.as_view(), name="task_delete"),
]