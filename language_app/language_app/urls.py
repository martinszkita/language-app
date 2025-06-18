from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vocabulary/', include('vocabulary.urls')), # pamietac o '/' !!!
    path('', views.home_page,name='home_page'),  # Assuming you have a home_page view in views.py
    path('<str:language_str>/', include('vocabulary.urls')),
    path('users/', include('users_app.urls')),
    path('users/', include('django.contrib.auth.urls')),  # For login/logout functionality
]
