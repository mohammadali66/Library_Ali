from django import forms
#from django.views.generic.edit import CreateView
from .models import Note


class AddNoteForm(forms.ModelForm):
    
    class Meta:    
        model = Note
        fields = ['pageOfBook',
                  'text',
              ]