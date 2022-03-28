from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE, SET_NULL, PROTECT, DateField, IntegerField, BooleanField, ManyToManyField, BigIntegerField
from rest_framework import serializers

class Book(Model):
    id = models.BigIntegerField(primary_key=True) # 플라이북 책 id
    image = CharField(max_length=400) # 이미지 URL
    title = CharField(max_length=400) # 책 제목
    isbn = CharField(max_length=200) # 책 ISBN
    author = CharField(max_length=200) # 책 저자
    publisher = CharField(max_length=200) # 책 출판사
    pubdate = DateField() # 책 출판일
    genre = CharField(max_length=200) # 책 장르
    intro = TextField() # 책 소개
    desc = TextField() # 책 설명
    desc_pub = TextField() # 출판사 책 설명
    desc_index = TextField() # 책 목차
    kdc = CharField(max_length=200) # KDC 번호
    category = CharField(max_length=200) # 카테고리 (KDC 대분류)
class User(Model):
    age = IntegerField()
    sex = CharField(max_length=100)
    is_love = CharField(max_length=100)
    job = CharField(max_length=200)
    
class Review(Model):
    book = ForeignKey('Book', on_delete=models.CASCADE, related_name='reviews')
    user = ForeignKey('User', on_delete=models.CASCADE, related_name='reviews')
    read_state = CharField(max_length=100)
    score = IntegerField()
    created_at = DateTimeField()