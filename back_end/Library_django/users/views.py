from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from . import forms

class UserRegisterView(View):
    template_name = 'users/register.html'
    
    def get(self, request, *args, **kwargs):
        
        form = forms.SignUpForm()
        context = {'form': form, }
        return render(request, self.template_name, context)
    
    #------------------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        
            return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})
    
