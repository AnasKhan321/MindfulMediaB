from rest_framework import serializers
from .models import Books, Order


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('Name', 'Category', 'image', 'Summary','url_img','Price')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'item', 'Price', 'Update', 'Address1', 'Address2', 'State', 'City')
