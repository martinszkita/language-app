from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login_user, name='login_user'),

]
