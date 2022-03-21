from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE, SET_NULL, PROTECT, DateField, IntegerField, BooleanField
from rest_framework import serializers

class Image(Model):
    url = CharField(max_length=100) # 외부 저장소 사용? + 검증 꼭 해야함

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    deleted_at = DateTimeField(null=True, blank=True)
class User(Model):
    name = CharField(max_length=100)
    phone = CharField(max_length=100)
    birthdate = DateField()
    password = CharField(max_length=100)
    user_type = IntegerField(default=0)
    is_buisness = BooleanField(default=False)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    deleted_at = DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'user'

class Address(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    address = TextField()
    is_default = BooleanField(default=False)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    deleted_at = DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'address'

'''
type:
* 0 = 공장
'''
class Shop(Model):
    owner = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=100)
    type = IntegerField(default=0)
    company_number = CharField(max_length=100)
    company_address = CharField(max_length=100)
    bank_account = CharField(max_length=100)
    bank_name = CharField(max_length=100)
    thumbnail = CharField(max_length=100)
    intro = TextField()
    description = TextField()
    accepted = BooleanField(default=False)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    deleted_at = DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'shop'

class Product(Model):
    shop = ForeignKey(Shop, on_delete=CASCADE)
    name = CharField(max_length=100)
    description = TextField()
    price = IntegerField()
    discount_price = IntegerField()

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    deleted_at = DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'product'

class ProductImage(Model):
    product = ForeignKey(Product, on_delete=CASCADE)
    image = ForeignKey(Image, on_delete=CASCADE)
    order = IntegerField()

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    deleted_at = DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'product_image'

class ProductOption(Model):
    product = ForeignKey(Product, on_delete=CASCADE)
    name = CharField(max_length=100)
    description = TextField()
    price = IntegerField()
    stock = IntegerField()
    order = IntegerField()

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    deleted_at = DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'product_option'

class CartItem(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    option = ForeignKey(ProductOption, on_delete=CASCADE)
    quantity = IntegerField()

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    deleted_at = DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'cart_item'
