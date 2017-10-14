from django.shortcuts import render
from django.views import View

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
    