from rest_framework import serializers

from books.models import Category, Book


    
#................................................................................................................
#Book Detail for Home page
class BookHomeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('title', 'slug', 'authors', 'image', 'featured')
        
        
#................................................................................................................
#Category detail for Home page
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

#................................................................................................................
#category detail
class CategoryDetailSerializer(serializers.ModelSerializer):
    
    category_books = BookHomeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ('name', 'slug', 'description', 'category_books', )

#................................................................................................................
#Book detail without pdf file
class BookDetailSerializer(serializers.ModelSerializer):
    
    category = CategoryMenuSerializer()
    
    class Meta:
        model = Book
        fields = ('title', 
                  'slug', 
                  'description', 
                  'authors', 
                  'publisher', 
                  'pageCount', 
                  'image', 
                  'category',
                  )

#................................................................................................................
#Book detail complete with pdf file
class BookDetailCompleteSerializer(serializers.ModelSerializer):
    
    category = CategoryMenuSerializer()
    
    class Meta:
        model = Book
        fields = ('title', 
                  'slug', 
                  'description', 
                  'authors', 
                  'publisher', 
                  'pageCount', 
                  'image',
                  'pdfFile', 
                  'category',
                  )


        
        
        