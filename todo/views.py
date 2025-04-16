from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from todo.models import TODO


def signup(request):
    if request.method == 'POST':
        frm = request.POST.get('frm')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        if User.objects.filter(username=frm).exists():
            return render(request, "signup.html", {"error": "Username already exists"})

        User.objects.create_user(username=frm, email=email, password=pwd)
        return redirect('/login')

    return render(request, "signup.html")


def login(request):
    if request.method == 'POST':
        frm = request.POST.get('frm')
        pwd = request.POST.get('pwd')

        userr = authenticate(request, username=frm, password=pwd)
        if userr is not None:
            auth_login(request, userr)
            return redirect('/todo')
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


def todo(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            TODO.objects.create(title=title, user=request.user)

    todos = TODO.objects.filter(user=request.user).order_by('-date')
    return render(request, "todo.html", {"todos": todos})


def logout_view(request):
    auth_logout(request)
    return redirect('/login')
