from django.urls import path
from . import views

urlpatterns = [
    path('', views.vocabulary_home,name='vocabulary_home'),
    path('word_list/',views.word_list,name='word_list'),
    path('add_word/', views.add_word, name='add_word'),
    # path('quiz', views.quiz, name='quiz'),
]
