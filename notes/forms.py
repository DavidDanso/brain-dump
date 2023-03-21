from django import forms
from django.forms import ModelForm
from .models import *

class QuickNoteCreationForm(ModelForm):
    class Meta:
        model = QuickNote
        fields = '__all__'
        exclude = ['account_owner']
        widgets = {
            'title': forms.TextInput(attrs={'id': 'note_title', 'placeholder': 'Untitled'}),
            'description': forms.Textarea(attrs={'id': 'note_paragraph', 'placeholder': '/start typing notes here...'}),
        }
    def __init__(self, *args, **kwargs):
        super(QuickNoteCreationForm, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'form-control'})




           
