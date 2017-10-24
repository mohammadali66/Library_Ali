from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from . import models
from . import forms
from users.models import UserProfile


class HomeView(View):
    template_name = 'home.html'
    
    def get(self, request, *args, **kwargs):
        
        #. . . . . . . . . . . . . . . . . .
        #get category list with their books those have featured==True
        categoryList = models.Category.objects.all()
        
        #category_book_list[(p1, [s1.1, s1.2]),  (p2, [s2.1, s2.2]), ]
        category_book_list = []
        
        for category in categoryList:
            try:
                book_list = models.Book.objects.filter(featured=True, category=category)
            except:
                book_list = None
                
            category_book_list.append((category, book_list))
        #. . . . . . . . . . . . . . . . . .
        
        context = {'category_book_list': category_book_list}
        return render(request, self.template_name, context)

#............................................................................................................    
class CategoryDetailView(View):
    
    template_name = 'books/category_detail.html'
    
    def get(self, request, slug, *args, **kwargs):
        
        errorMessage = None
        
        try:
            category = models.Category.objects.get(slug=slug)            
            book_list = models.Book.objects.filter(category=category)
            
            page = request.GET.get('page', 1)
            paginator = Paginator(book_list, 2)
            
        except:
            book_list = None
            category = None
            errorMessage = 'Not Found!'
        
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        
        context = {'category': category, 'books': books }
        return render(request, self.template_name, context)


#............................................................................................................
class BookDetailView(View):
    
    template_name = 'books/book_detail.html'
    isLogged = False        #is user logged in
    isSelected = False      #is logged user selected the book before
    noteList = None
    #addForm = None
    
    def get(self, request, slug, *args, **kwargs):
        
        try:            
            if request.user.is_authenticated():
                self.isLogged = True
                userProfile = UserProfile.objects.get(user=request.user,
                                                      books__slug=slug)
                #List of Notes
                self.noteList = models.Note.objects.filter(user=request.user,
                                               book__slug=slug)
                
                #forms for add note
                #self.addForm = forms.AddNoteForm() 
                
                 
                self.isSelected = True
            else:
                self.isLogged = False
                
        except UserProfile.DoesNotExist:
            userProfile = None
            self.isSelected = False
                                            
        try:
            book = models.Book.objects.get(slug=slug)
        except models.Book.DoesNotExist:
            book = None
            
        context = {'book': book,
                   'noteList': self.noteList, 
                   #'addForm': self.addForm,
                   'isLogged': self.isLogged, 
                   'isSelected': self.isSelected,                   
                   }
        
        return render(request, self.template_name, context)
    
    
    
    def post(self, request, slug, *args, **kwargs):
        message=''
        
        if  not request.POST['pageOfBook'] or not request.POST['text']:
            message = "some fields are empty!"
        else:
            note = models.Note(
                        pageOfBook = request.POST['pageOfBook'],
                        text = request.POST['text'],
                        user = request.user,
                        book = models.Book.objects.get(slug=slug)
                        )
            note.save()
            message = 'successfully added'
        
        # .......  get method
        try:            
            if request.user.is_authenticated():
                self.isLogged = True
                userProfile = UserProfile.objects.get(user=request.user,
                                                      books__slug=slug)
                #List of Notes
                self.noteList = models.Note.objects.filter(user=request.user,
                                               book__slug=slug)
                
                #forms for add note
                #self.addForm = forms.AddNoteForm() 
                
                 
                self.isSelected = True
            else:
                self.isLogged = False
                
        except UserProfile.DoesNotExist:
            userProfile = None
            self.isSelected = False
                                            
        try:
            book = models.Book.objects.get(slug=slug)
        except models.Book.DoesNotExist:
            book = None
            
        context = {'book': book,
                   'noteList': self.noteList, 
                   #'addForm': self.addForm,
                   'isLogged': self.isLogged, 
                   'isSelected': self.isSelected,
                   'message': message,
                   }
        
        return render(request, self.template_name, context)
                
             
#............................................................................................................
class AddBookToBooksListView(View):
    
    message = ''
    
    def get(self, request, slug, *args, **kwargs):
        
        if request.user.is_authenticated():
            try:
                userProfile = UserProfile.objects.get(user=request.user,
                                                      books__slug=slug)
                self.message = 'before added!!'
            except UserProfile.DoesNotExist:
                try:
                    book = models.Book.objects.get(slug=slug)
                    userProfile = UserProfile.objects.get(user=request.user)
                    userProfile.books.add(book)
                    userProfile.save()
                    self.message = 'success!!'
                except:
                    self.message = 'book not found!!'
                    
        return redirect('bookclassic:bookdetail', slug=slug)

#............................................................................................................
class UpdateDeleteNoteView(View):
    
    def get(self, request, bookslug, pk, *args, **kwargs):
        
        if request.user.is_authenticated():
            try:
                note = models.Note.objects.get(pk=pk)
                print str(note)
                note.delete()
            except:
                pass
            
        return redirect('bookclassic:bookdetail', slug=bookslug)





