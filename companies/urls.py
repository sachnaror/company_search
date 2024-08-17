# Your urls configuration here
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search_results'),
    path('company/<str:registration_number>/', views.company_detail, name='company_detail'),
]
