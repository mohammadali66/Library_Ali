from rest_framework import serializers, fields

from .models import Category, Book

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description']
        
        
#................................................................................................................
class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('title', 'slug', 'category', 'description', 'authors',
                   'publisher', 'pageCount', 'image', 'pdfFile', 'featured' )
        
        
#................................................................................................................
class CategoryByBooksSerializer(serializers.ModelSerializer):
    
    category_books = BookSerializer(read_only=True, many=True)
    
    class Meta:
        model = Category
        fields = ('name', 'slug', 'category_books')
        
        
        
        
        