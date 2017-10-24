# encoding: utf-8
#very important: encoding should set in first line

from django.contrib import admin
from django.utils import timezone

from .models import Book, Category, Note

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    fields = ['name', 'slug', 'description']
    
    #create slug
    prepopulated_fields = {"slug" : (unicode("name"),),}
    
admin.site.register(Category, CategoryAdmin)

#.....................................................................................................................
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'pageCount', 'created_datetime', 'updated_datetime', 'featured']    
    fields = ['title', 'slug', 'category', 'description', 'authors', 'publisher', 'pageCount', 'image', 'pdfFile',
              'created_datetime', 'updated_datetime', 'featured' ]
    
    #create slug
    prepopulated_fields = {"slug" : (unicode("title"),),}
    readonly_fields = ['created_datetime',]
    
    
    def save_model(self, request, obj, form, change):
                            
        #update datetime publication
        obj.updated_datetime = timezone.now()
                
        obj.save()
    
        
admin.site.register(Book, BookAdmin)

#.....................................................................................................................

admin.site.register(Note)
