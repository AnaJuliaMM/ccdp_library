from rest_framework import serializers
from .models import Category, Book

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        # Extract category data from validated_data and create/update the category
        category_data = validated_data.pop('category')
        category_instance, _ = Category.objects.get_or_create(**category_data)

        # Create the book with the associated category
        book_instance = Book.objects.create(category=category_instance, **validated_data)
        return book_instance

    
