from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions

from . import serializers
from books.models import Book, Category, Note
from users.models import UserProfile


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
class BooksOfLoggedUserAPIView(generics.ListAPIView):
    
    serializer_class = serializers.BookHomeSerializer
    permission_classes = (permissions.IsAuthenticated, )
    
    def get_queryset(self):
        userProfile = UserProfile.objects.get(user = self.request.user)
        bookList = Book.objects.filter(book_users = userProfile)
        return bookList
        
        
        
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
            
#................................................................................................................
#Book Detail
class BookDetailAPIView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, slug, format=None):
        
        try:
            #request.user - - request.auth
            if request.auth:
                userProfile = UserProfile.objects.get(user=request.user,
                                                      books__slug=slug)
            else:
                userProfile = None
                
        except UserProfile.DoesNotExist:
            userProfile = None
        
        try:            
            book = Book.objects.get(slug=slug)
            
            #if is authenticated and the book is in books list of logged user
            if userProfile:
                serializer = serializers.BookDetailCompleteSerializer(book, context={'user_id':request.user.id})
                #serializer = serializers.BookDetailCompleteSerializer(book)
            else:
                serializer = serializers.BookDetailSerializer(book)
                
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'errorMessage': 'Not Found!!'}, status=status.HTTP_404_NOT_FOUND)
        
        
#................................................................................................................
#Add book to books list of logged user
class AddBookToBooksListUserAPIView(APIView):
    
    #serializer_class = serializers.BookHomeSerializ1r
    permission_classes = (permissions.IsAuthenticated, )
    message = ''
    
    def get(self, request, slug, format=None):
                
        try:            
            userProfile = UserProfile.objects.get(user=request.user, books__slug=slug)
            self.message = 'before added!!'
            return Response({'message': self.message }, status=status.HTTP_400_BAD_REQUEST)
        except:
            try:
                book = Book.objects.get(slug=slug)
                userProfile = UserProfile.objects.get(user=request.user)
                userProfile.books.add(book)
                userProfile.save()
                
                self.message = 'success!!'
                return Response({'message': self.message }, status=status.HTTP_202_ACCEPTED)
                
            except:
                self.message = 'book not found!!'
                return Response({'message': self.message }, status=status.HTTP_400_BAD_REQUEST)
            
        
#................................................................................................................
class NoteAPIView(APIView):
                
    serializer_class = serializers.NoteSerializer
    permission_classes = (permissions.IsAuthenticated, )
    
    def post(self, request, bookslug):
        
        serializer = serializers.NoteSerializer(data = request.data)
        if serializer.is_valid():
            try:
                userProfile = UserProfile.objects.get(user=request.user, books__slug=bookslug)
                
                note = Note(
                            user = userProfile.user,
                            book = Book.objects.get(slug=bookslug),
                            text = request.data.get('text'),
                            pageOfBook = request.data.get('pageOfBook')
                        )                
                note.save()
                
                serializer = serializers.NoteSerializer(note)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                
            except UserProfile.DoesNotExist:
                return Response({'message': 'You have not permission to add note to this book' }, 
                                status=status.HTTP_400_BAD_REQUEST)           
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
            
#................................................................................................................
class NoteUpdateDeleteAPIView(APIView):
    serializer_class = serializers.NoteSerializer
    permission_classes = (permissions.IsAuthenticated, )
    
    def delete(self, request, pk):
        try:
            note = Note.objects.get(pk=pk)
            
            #just user of note can delete that.
            if note.user == request.user:
                note.delete()
                return Response({'message': 'deleting successfully.'})                
            else:
                return Response({'error message': 'You have not permission.'})
            
        except Note.DoesNotExist:
            return Response({'error message': 'This note does not exist.'})
        
            
            
            