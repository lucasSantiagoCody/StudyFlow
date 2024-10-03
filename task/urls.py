from django.urls import path
from . import views

urlpatterns = [
    path('home-page/', views.home_view, name='home-url')
]