from rest_framework import serializers

from books.models import Book, Category, Note


    
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
class NoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Note
        fields = ('id', 
                  'user',
                  'book',
                  'text',
                  'pageOfBook',
                  'created_datetime',
                  'updated_datetime',
                  ) 
        extra_kwargs = {
                        'id'              : {'read_only': True},
                        'user'            : {'read_only': True},
                        'book'            : {'read_only': True},
                        'created_datetime': {'read_only': True},
                        'updated_datetime': {'read_only': True},
                        }
    
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
    notes = serializers.SerializerMethodField('get_book_notes')
    
    def get_book_notes(self, book):
        #request=self.context['request']
        user_id = self.context['user_id']
        print 'id %s' % user_id
        notes = Note.objects.filter(book=book, user__pk=user_id)
        serializer = NoteSerializer(instance=notes, many=True)        
        return serializer.data
    
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
                  'notes',
                  )
        