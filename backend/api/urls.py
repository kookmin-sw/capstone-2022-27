from django.urls import path

from .views import base, book, user

urlpatterns = [
    path('user/register/', user.register),
    path('user/login/', user.login),
    
    path('book/detail/<int:id>', book.detail),
]