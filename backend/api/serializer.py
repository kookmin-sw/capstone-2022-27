from rest_framework import serializers
from .models import Book, User, Review

class SimpleSerializer(serializers.Serializer):
    content = serializers.JSONField()
    
class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'image', 'title', 'isbn', 'author', 'publisher', 'pubdate', 'genre', 'intro', 'desc', 'desc_pub', 'desc_index', 'category', 'kdc')
        read_only_fields = ('id',)

class BookSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'image', 'title', 'isbn', 'author', 'publisher', 'pubdate')
        read_only_fields = ('id',)

class BookDetailSerializer(serializers.Serializer):
    book = BookSerializer()
    similar = BookSimpleSerializer(many=True)
    keywords = serializers.ListField(child=serializers.CharField())
    
class BookLineSerializer(serializers.Serializer):
    title = serializers.CharField()
    desc = serializers.CharField()
    books = BookSimpleSerializer(many=True)
    

# 리뷰 시리얼라이저는 유저정보도 담기
# 책 detail에 리뷰 넣기