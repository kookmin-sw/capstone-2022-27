from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE, SET_NULL, PROTECT, DateField, IntegerField, BooleanField, ManyToManyField, BigIntegerField
from rest_framework import serializers

class Book(Model):
    id = models.BigIntegerField(primary_key=True) # 플라이북 책 id
    image = CharField(max_length=400, blank=True) # 이미지 URL
    title = CharField(max_length=400) # 책 제목
    isbn = CharField(max_length=200) # 책 ISBN
    author = CharField(max_length=200) # 책 저자
    publisher = CharField(max_length=200) # 책 출판사
    pubdate = DateField() # 책 출판일
    genre = CharField(max_length=200, blank=True) # 책 장르
    intro = TextField(blank=True) # 책 소개
    desc = TextField(blank=True) # 책 설명
    desc_pub = TextField(blank=True) # 출판사 책 설명
    desc_index = TextField(blank=True) # 책 목차
    kdc = CharField(max_length=200, blank=True) # KDC 번호
    category = CharField(max_length=200, blank=True) # 카테고리 (KDC 대분류)
    num_review = IntegerField(default=0) # 리뷰 수
    
class User(Model):
    age = IntegerField(blank=True, null=True)
    sex = CharField(max_length=100, null=True, blank=True)
    is_love = CharField(max_length=100, null=True, blank=True)
    job = CharField(max_length=200, null=True, blank=True)
    booka = BooleanField(default=False)
    username = CharField(max_length=200, null=True, blank=True)
    nickname = CharField(max_length=200, null=True, blank=True)
    password = CharField(max_length=400, null=True, blank=True)
    
class Review(Model):
    book = ForeignKey('Book', on_delete=models.CASCADE, related_name='reviews')
    user = ForeignKey('User', on_delete=models.CASCADE, related_name='reviews')
    read_state = CharField(max_length=100)
    score = IntegerField()
    created_at = DateTimeField(auto_now_add=True, blank=True)
    content = TextField(null=True, default='')

class Keyword(Model):
    book = ForeignKey(Book, on_delete=models.CASCADE, related_name='keywords')
    keyword = CharField(max_length=100)
    
    def __str__(self):
        return self.keyword
    