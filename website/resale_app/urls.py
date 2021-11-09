from django.urls import path

from . import views

urlpatterns = [
    path('', views.search_page, name='search_page'),
    path('search_result/', views.search_result, name='search_result'),
    path('ajax/get_categories_available/', views.get_categories_available, name='get_categories_available'),
]