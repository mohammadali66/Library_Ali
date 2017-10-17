from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from . import models

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





