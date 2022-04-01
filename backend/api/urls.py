from django.urls import path

from .views import base, book

urlpatterns = [
    path('book/detail/<int:id>', book.detail),
]