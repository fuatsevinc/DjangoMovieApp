from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movie", views.movie, name="movie"),
    path("movie/<slug:slug>", views.movie_detail),
    
    
    ]