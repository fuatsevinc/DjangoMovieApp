from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html" )

def movie(request):
    return render(request, "movie.html")

def movie_detail(request, slug):
    return render(request, "movie_detail.html", {
        "slug":slug
    })

