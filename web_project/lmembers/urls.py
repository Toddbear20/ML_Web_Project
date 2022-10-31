from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('naver/', views.naver, name='naver'),
    path('naver_search/', views.lmembers_surprise, name='naver_search'),     
]