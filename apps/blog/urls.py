from django.urls import path
from .views import blog_page, about_page, blogsingle
urlpatterns = [
    path('', blog_page),
    path('about/', about_page),
    path('single/<int:pk>/', blogsingle)
]