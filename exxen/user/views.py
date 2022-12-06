from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
# Create your views here.
def userRegister(request):
    form = UserCreate()
    if request.method == "POST":
        form = UserCreate(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.first_name = user.username
            user.save()
            messages.success(request, "Kaydınız oluşturuldu")
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, "register.html", context)

def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Giriş yapıldı")
            return redirect('index')
        else:
            messages.error(request, "Böyle bir kullanıcı bulunmamakta")
    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    messages.success(request, "Çıkış yapıldı")
    return redirect('index')