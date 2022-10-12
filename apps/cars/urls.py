from django.urls import path
from .views import home_page, car, rent

urlpatterns = [
    path('', home_page),
    path('cars/', car),
    path('rent/<int:pk>/', rent),


]