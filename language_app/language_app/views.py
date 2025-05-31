from django.shortcuts import render
from django.http import request

def home_page(reqest):
    return render(request, 'language_app/home.html')
    