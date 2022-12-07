from django.urls import path

from . import views

urlpatterns = [
    path('task/', views.task_list.as_view(), name="task"),
    path('task/title/', views.task_list_filter_title.as_view(), name="task_list_filter_title"),
    path('task/add/', views.task_post.as_view(), name="task_post"),
    path('task/complete/', views.task_list_complete.as_view(), name="task_list_complete"),
    path('task/uncomplete/', views.task_list_uncomplete.as_view(), name="task_list_uncomplete"),
    path('task/list/', views.view_all_task_from_list.as_view(), name="view_all_task_from_list"),
    path('task/desc/', views.view_all_task_filter_desc.as_view(), name="view_all_task_filter_desc"),
    path('task/<int:pk>/', views.task_detail.as_view(), name="task_detail"),
    path('task/put/<int:pk>/', views.task_put.as_view(), name="task_update"),
    path('task/delete/<int:pk>/', views.task_delete.as_view(), name="task_delete"),

    path('list/', views.list_view.as_view(), name="list_view"),
    path('list/name/', views.list_view_filter_name.as_view(), name="list_view_filter_name"),
    path('list/add/', views.list_post.as_view(), name="list_post"),
    path('list/put/<int:pk>/', views.list_put.as_view(), name="list_put"),
    path('list/delete/<int:pk>/', views.list_delete.as_view(), name="list_delete"),
    path('list/date/', views.view_all_list_date.as_view(), name="view_all_list_date"),
]