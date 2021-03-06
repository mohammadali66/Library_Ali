from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

from . import forms


#...........................................................................................................
class UserRegisterView(View):
    template_name = 'users/register.html'
    
    def get(self, request, *args, **kwargs):
                
        if request.user.is_authenticated():
            #if user before logged in
            return redirect('home')
        else:
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
    
#...........................................................................................................
class UserLoginView(View):
    template_name = 'users/login.html';
    
    def get(self, request, *args, **kwargs):
        
        if request.user.is_authenticated():
            #if user before logged in
            return redirect('home')
        else:
            context = {}
            return render(request, self.template_name, context)
    
    #------------------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        
        print(str(request.POST['username']))
        
        if not request.POST['username'] or not request.POST['password']:
            errorMessage = 'Please fill the fields.'
            context = {'errorMessage': errorMessage}
            return render(request, self.template_name, context)
        else:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            
            if user is not None:
                login(request, user)
                context = {}
                #return render(request, 'home.html', context)
                return HttpResponseRedirect("/classic/")
            else:
                errorMessage = 'Your username and password are incorrect!'
                context = {'errorMessage': errorMessage}
                return render(request, self.template_name, context)
        
#...........................................................................................................
class UserLogoutView(View):
    
    def get(self, request, *args, **kwargs):
        
        logout(request)
        return redirect('home')
        
        
    
    