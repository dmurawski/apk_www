from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('osoby/', views.osoba_list.as_view()),
    path('osoby/<int:pk>/', views.osoba_detail.as_view()),
    path('druzyny/', views.druzyna_list),
    path('druzyny/<int:pk>/', views.druzyna_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)