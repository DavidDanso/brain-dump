from django import forms
from django.forms import ModelForm
from .models import *

# folders form
class FolderNameCreationForm(ModelForm):
    class Meta:
        model = FolderName
        fields = '__all__'
        exclude = ['number_of_notes', 'account_owner']
        # add id and placeholder to the input field
        widgets = {
            'title': forms.TextInput(attrs={'id': 'inputFolderName', 'placeholder': 'enter new folder name...'}),
        }
    # add class to the input field
    def __init__(self, *args, **kwargs):
        super(FolderNameCreationForm, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'form-control'})

# notes form
class NoteCreationForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        exclude = ['name']
        # add id and placeholder to the input field
        widgets = {
            'title': forms.TextInput(attrs={'id': 'note_title', 'placeholder': 'Untitled'}),
            'description': forms.Textarea(attrs={'id': 'note_paragraph', 'placeholder': '/start typing notes here...'}),
        }
    # add class to the input field
    def __init__(self, *args, **kwargs):
        super(NoteCreationForm, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'form-control'})
           
