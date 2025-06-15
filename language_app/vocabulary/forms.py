# vocabulary/forms.py
from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['name', 'polish_translation']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter word'}),
            'polish_translation': forms.TextInput(attrs={'placeholder': 'Enter Polish translation', 'required': False}),
        }
