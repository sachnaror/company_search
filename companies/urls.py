from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('suggestions/', views.search_suggestions, name='search_suggestions'),
    path('company/<str:registration_number>/', views.company_detail, name='company_detail'),
]
