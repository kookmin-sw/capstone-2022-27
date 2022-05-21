from django.urls import path

from .views import base, book, user

urlpatterns = [
    path('user/register/', user.register),
    path('user/login/', user.login),
    
    path('book/detail/<int:id>', book.detail),
    path('book/review_pages/<int:id>/<int:page>', book.review_pages),
    path('book/search_keyword/<keyword>/<int:page>', book.search_keyword),
    path('book/search/<keyword>/<int:page>', book.search),
    path('book/firstpage', book.firstpage),
    path('book/firstpage_list/', book.firstpage_list),
    path('book/review/', book.review),
    path('book/recommend/<int:recom_type>', book.recommend),
    
    path('book/banners', book.banners),
]