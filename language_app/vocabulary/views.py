from django.shortcuts import render
from django.db import models
from .models import Word, Language

# Create your views here.
def display_words(request):
    words = Word.objects.all()
    return render(request, 'word_list.html', {'words' : words})

def vocabulary_home(request):
    return render(request, 'vocabulary_home.html')
    