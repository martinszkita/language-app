from django.shortcuts import render, redirect, get_object_or_404
from .models import Word, Language
from .forms import WordForm
from django.contrib import messages
from django.urls import resolve

def word_list(request, language_str):

    language_obj = get_object_or_404(Language, name=language_str)
    words = Word.objects.filter(language=language_obj)
    
    return render(
        request,
        'vocabulary/word_list.html',
        {
            'language': language_obj.name,
            'words': words,
        },
    )



def vocabulary_home(request, language_str):
    return render(request, 'vocabulary/vocabulary_home.html', {'language': language_str})

def add_word(request, language_str):
    language_obj = get_object_or_404(Language, name=language_str)
    
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.language = language_obj
            word.save()
            messages.success(request, f"Word '{word.name}' added successfully!")
            return redirect('add_word', language_str=language_str)
    else:
        form = WordForm()
    
    return render(
        request,
        'vocabulary/add_word.html',
        {
            'form': form,
            'language': language_obj.name,
        },
    )