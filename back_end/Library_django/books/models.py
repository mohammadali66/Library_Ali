# encoding: utf-8
#very important: encoding should set in first line

from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from __builtin__ import str
from django.utils import timezone

from django.contrib.auth.models import User


class Category(models.Model):
    name         = models.CharField(max_length=50)
    description  = models.TextField(blank=True, null=True)
    slug         = models.SlugField(unique=True, null=True, allow_unicode=True)
    
    def __unicode__(self):
        return unicode(self.name)
    
    class Meta:
        unique_together = ('name', 'slug')
        
    def get_absolute_url(self):
        return reverse('bookclassic:categorydetail', kwargs={'slug': self.slug})

#.................................................................................................................
class Book(models.Model):
    title               = models.CharField(max_length=100)
    slug                = models.SlugField(unique=True, null=True, allow_unicode=True)
    
    category            = models.ForeignKey(Category, related_name='category_books',on_delete=models.CASCADE)
    description         = RichTextField(null=True, blank=True)
    
    authors             = models.CharField(max_length=150, null=True, blank=True)
    publisher           = models.CharField(max_length=50, null=True, blank=True)
    pageCount           = models.IntegerField(default=0, null=False, blank=False)
    
    
    image               = models.ImageField(upload_to="imageBook", null=True, blank=True)
    pdfFile             = models.FileField(upload_to="fileBook", null=True, blank=True)
        
    created_datetime    = models.DateTimeField(auto_now_add = True, auto_now = False)
    #updated_datetime   = models.DateTimeField(auto_now_add = False, auto_now = False)
    updated_datetime    = models.DateTimeField(default = timezone.now) 
    
    featured            = models.BooleanField(default=False)
    
    
    def __unicode__(self):
        return unicode(self.title)
    
    class Meta:
        unique_together = ('title', 'slug')
        
        
    def get_absolute_url(self):
        return reverse('bookclassic:bookdetail', kwargs={'slug': self.slug})
     

#................................................................................................................

class Note(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    book                = models.ForeignKey(Book, related_name='note_books', on_delete=models.CASCADE) 
    text                = RichTextField(null=True, blank=True)
    pageOfBook          = models.CharField(max_length=50)
    created_datetime    = models.DateTimeField(auto_now_add = True, auto_now = False)
    #updated_datetime   = models.DateTimeField(auto_now_add = False, auto_now = False)
    updated_datetime    = models.DateTimeField(default = timezone.now)
    
    
    def __unicode__(self):
        return 'note {0} of user: {1} for book: {2}'.format(self.id, self.user, self.book)
    
    
    
    