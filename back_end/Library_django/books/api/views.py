from rest_framework import status
from rest_framework.decorators import api_view
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
    




            