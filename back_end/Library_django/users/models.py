from __future__ import unicode_literals

from django.db import models

# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.models import BaseUserManager

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from books.models import Book

#.........................................................................................................
#create Token for each user

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    
#.........................................................................................................
class UserProfile(models.Model):
    
    education  = models.CharField(max_length=100, default='')
    user       = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
    books      = models.ManyToManyField(Book, related_name='book_users', null=True, blank=True)
        
    
    def __unicode__(self):
        return self.user.username
#.........................................................................................................
# class UserProfileManager(BaseUserManager):
#     """ Hleps Django work with our custom user model. """
#     
#     def create_user(self, username, email, password=None):
#         """ Creates a new user profile object. """
#         
#         if not email:
#             raise ValueError("Users must have an email address.")
#         
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email)
#         
#         user.set_password(password)
#         
#         return user
#     
#     
#     def create_superuser(self, username, email, password):
#         """ Creates and saves a new superuser with given details. """
#         
#         user = self.create_user(username, email, password)
#         
#         user.is_superuser = True
#         user.is_staff = True
#         
#         user.save(using=self._db)
#         
#         return user
#         
#                 
# #-------------------------------------------------------------------------------------------------------
# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     """ Respents a "user profile" inside our system. """
#     
#     username     = models.CharField(max_length=255, unique=True)
#     first_name   = models.CharField(max_length=100)
#     last_name    = models.CharField(max_length=100)
#     email        = models.EmailField(max_length=255, unique=True)
#     
#     is_active    = models.BooleanField(default=True)
#     is_staff     = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     
#     books        = models.ManyToManyField(Book, related_name='book_users')
#     
#     objects = UserProfileManager()
#     
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email',]
#     
#     def get_full_name(self):
#         """ Used to get a users full name. """
#         return "{0} {1}".format(self.first_name, self.last_name)
#     
#     
#     def get_short_name(self):
#         """ used to get users short name. """
#         return self.first_name
#     
#     
#     def __unicode__(self):
#         """ Django uses this when it needs to convert the object to a string. """
#         return self.username
    




