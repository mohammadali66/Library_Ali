from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
 
from . import models
 
class UserProfileInline(admin.StackedInline):
    model = models.UserProfile
    can_delete = False
    verbose_name_plural = 'userProfile'
 
#.......................................................................................................
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )
     
     
#Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
