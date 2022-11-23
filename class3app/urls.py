from django.urls import path
from . import views

urlpatterns = [
    path('osoby/', views.osoba_list.as_view()),
    path('osoby/<int:pk>/', views.osoba_detail.as_view()),
    path('osoby/put/<int:pk>/', views.osoba_put.as_view()),
    path('osoby/delete/<int:pk>/', views.osoba_delete.as_view()),
    path('druzyny/', views.druzyna_list),
    path('druzyny/<int:pk>/', views.druzyna_detail),
    path('test/<int:pk>/', views.person_view),
]
urlpatterns += [
    path('api-token-auth/', views.CustomAuthToken)
]