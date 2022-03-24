from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE, SET_NULL, PROTECT, DateField, IntegerField, BooleanField
from rest_framework import serializers

class Book(Model):
    image = CharField(max_length=400) # 이미지 URL
    title = CharField(max_length=400) # 책 제목
    isbn = CharField(max_length=200) # 책 ISBN
    author = CharField(max_length=200) # 책 저자
    publisher = CharField(max_length=200) # 책 출판사
    pubdate = DateField() # 책 출판일
    genre = IntegerField() # 책 장르
    intro = TextField() # 책 소개
    desc = TextField() # 책 설명
    desc_pub = TextField() # 출판사 책 설명
    desc_index = TextField() # 책 목차
