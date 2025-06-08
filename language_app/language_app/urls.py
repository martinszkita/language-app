from django.contrib import admin
from django.urls import path, include
from . import views
from vocabulary import views as vocabulary_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vocabulary/', include('vocabulary.urls')), # pamietac o '/' !!!
    path('<str:language>/word_list/', vocabulary_views.display_words, name='word_list'),
    path('', views.home_page,name='home_page'),  # Assuming you have a home_page view in views.py
    path('<str:language>/', include('vocabulary.urls')),
]
