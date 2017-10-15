from rest_framework import serializers

from books.models import Category, Book


    
#................................................................................................................
class BookHomeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('title', 'slug', 'image', 'featured')
        
        
#................................................................................................................
class CategoryHomeSerializer(serializers.ModelSerializer):
    
    books = serializers.SerializerMethodField('get_category_books')
    
    def get_category_books(self, category):
        books = Book.objects.filter(featured=True, category=category)
        serializer = BookHomeSerializer(instance=books, many=True)
        return serializer.data
    
    class Meta:
        model = Category
        fields = ('name', 'slug', 'books')
        
#................................................................................................................
#category list for menu
class CategoryMenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('name', 'slug')
   
        
        
        