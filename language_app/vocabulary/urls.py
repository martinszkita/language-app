from django.urls import path
from . import views

urlpatterns = [
    path('word_list/',views.display_words,name='word_list'),
    path('', views.vocabulary_home,name='vocabulary_home'),
]
