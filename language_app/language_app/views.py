from django.shortcuts import render
from django.http import request
from vocabulary.models import Language

def home_page(request):
    languages = Language.objects.all()
    return render(request, 'language_app/home.html', {'languages': languages})
    