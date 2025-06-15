from django.shortcuts import render, redirect, get_object_or_404
from .models import Word, Language
from .forms import WordForm
from django.contrib import messages
from django.urls import resolve

# Create your views here.
def word_list(request, language):
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

def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            # lang = resolve(request.path_info).kwargs.get('language').lower()
            word.language = Language.objects.get(name='German')  
            #word.language = resolve(request.path_info).kwargs.get('language')
            form.save()
            
            messages.success(request, "Słowo zostało pomyślnie dodane.")
            return redirect('add_word')  # lub inna strona po dodaniu
    else:
        form = WordForm()
        
    return render(request, 'vocabulary/add_word.html', {'form': form})

    