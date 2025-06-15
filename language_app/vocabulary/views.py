from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import Word, Language
from .forms import WordForm
from django.contrib import messages
from django.urls import resolve

# Create your views here.
def display_words(request, language=None):
    """Display words for the selected language."""
    if language is None:
        language = resolve(request.path_info).kwargs.get('language')

    language_obj = get_object_or_404(Language, name__iexact=language)
    words = Word.objects.filter(language=language_obj)
    return render(
        request,
        'vocabulary/word_list.html',
        {
            'language': language_obj.name,
            'words': words,
        },
    )


def vocabulary_home(request, language):
    return render(request, 'vocabulary/vocabulary_home.html', {'language': language})

def add_word(request, language=None):
    """Add a new word. Works with or without language in the URL."""
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Słowo zostało pomyślnie dodane.")
            if language:
                return redirect('add_word', language=language)
            return redirect('add_word')
    else:
        form = WordForm()
    return render(request, 'vocabulary/add_word.html', {'form': form, 'language': language})

    