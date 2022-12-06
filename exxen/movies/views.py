from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Film eklendi")
    context = {
        'movie':movies,
        
    }
    return render(request, "exxen.html", context)

def olustur(request):
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Film eklendi")
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, "create.html", context)