from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions

from . import serializers
from books.models import Category, Book


class CategoryBooksHomeAPIView(generics.ListAPIView):
    
    serializer_class = serializers.CategoryHomeSerializer
    permission_classes = (permissions.AllowAny, )
    
    def get_queryset(self):
        
        #categoryList = Category.objects.filter(category_books__featured=True).distinct()
        categoryList = Category.objects.all()        
        return categoryList
    


#................................................................................................................
#category list for menu
class CategoryMenuAPIView(generics.ListAPIView):
    
    serializer_class = serializers.CategoryMenuSerializer
    permission_classes = (permissions.AllowAny, )
    queryset = Category.objects.all()

#................................................................................................................
#category detail
class CategoryDetailAPIView(APIView):
    
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, slug, format=None):
        
        try:
            category = Category.objects.get(slug=slug)
            serializer = serializers.CategoryDetailSerializer(category)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#................................................................................................................
#books list of a category
class BooksOfOneCategoryAPIView(generics.ListAPIView):

    serializer_class = serializers.BookHomeSerializer
    permission_classes = (permissions.AllowAny, )
    
    def get_queryset(self):
            bookList = Book.objects.filter(category__slug=self.kwargs.get('categoryslug'))
            return bookList        

#     def get(self, request, categoryslug, format=None):
#         try:
#             bookList = Book.objects.filter(category__slug=categoryslug)
#             serializer = serializers.BookHomeSerializer(bookList, many=True)
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         except:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#................................................................................................................
#detail category
class CategoryDetailBriefAPIView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, slug, format=None):
        
        try:
            category = Category.objects.get(slug=slug)
            serializer = serializers.CategoryMenuSerializer(category)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
            