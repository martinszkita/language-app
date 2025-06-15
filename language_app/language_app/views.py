from django.shortcuts import render
from vocabulary.models import Language


def home_page(request):
    """Render the home page with a list of available languages."""
    languages = Language.objects.all()
    return render(request, 'language_app/home.html', {'languages': languages})
