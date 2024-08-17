from django.urls import path

from .views import company_detail, index, search

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
    path('company/<str:registration_number>/', company_detail, name='company_detail'),
]
