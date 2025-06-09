from django.shortcuts import render, redirect
from django.db import models
from .models import Word, Language
from .forms import WordForm
from django.contrib import messages
from django.urls import resolve

# Create your views here.
def word_list(request):
    language = resolve(request.path_info).kwargs.get('language')
    print("chosen language:", language)
    words = Word.objects.all
    return render(request, 'vocabulary/word_list.html', {'language': language, 'words': words})


def vocabulary_home(request, language):
    return render(request, 'vocabulary/vocabulary_home.html', {'language': language})

def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Słowo zostało pomyślnie dodane.")
            return redirect('add_word')  # lub inna strona po dodaniu
    else:
        form = WordForm()
    return render(request, 'vocabulary/add_word.html', {'form': form})

    