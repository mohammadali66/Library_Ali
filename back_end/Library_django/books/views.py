from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .serializers import CategorySerializer, BookSerializer, CategoryByBooksSerializer
from .models import Category, Book


@api_view(['GET'])
def getBookDetail(request, slug):
    
    if request.method == "GET":
        try:            
            book = Book.objects.get(slug=slug)
            serializer = BookSerializer(book)
            print "get boooo"
            return Response(serializer.data)
        
        except Book.DoesNotExist:            
            return Response(status = status.HTTP_404_NOT_FOUND)

#................................................................................................................
@api_view(['GET'])
def getBooksByCategory(request, categorySlug):
    
    if request.method == "GET":
        try:
            myCategory = Category.objects.get(slug=categorySlug)
            print str(myCategory)
            #bookList = Book.objects.filter(category=myCategory)
            #serializer = BookSerializer(bookList, many=True)
            serializer = CategoryByBooksSerializer(myCategory)
            return Response(serializer.data)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
#................................................................................................................
@api_view(['GET'])
def getBooksByCategories(request):
    if request.method == "GET":
        try:
            categoryList = Category.objects.all()            
            #categoryList = Category.objects.filter(category_books__featured=True)
            
            serializer = CategoryByBooksSerializer(categoryList, many=True)
            #serializer = CategoryByBooksSerializer(categoryList)
            
            return Response(serializer.data)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
            
#................................................................................................................
#@api_view(['GET'])
class view2(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    #queryset = Category.objects.filter(category_books__featured=True)
    serializer_class = CategoryByBooksSerializer





            