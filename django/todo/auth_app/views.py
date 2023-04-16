from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


# method == 'POST' or method == 'GET'

def login_view(request: WSGIRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user: User = authenticate(
            request,
            username=username,
            password=password
        )
        if user is None:
            return render(request, 'login.html', {
                'error_message': 'Неправильный логин или пароль',
            })

        login(request, user)
        return redirect('todo_main')

    return render(request, 'login.html')


def registration(request: WSGIRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        email = request.POST['email']

        user = User.objects.filter(
            username=username,
            password=password,
            email=email,
        )
        if password != password_confirm:
            return render(request, 'registration.html', {
                'error_message': 'Пароли не совпадают',
            })

    return render(request, 'registration.html')


def user_list(request: WSGIRequest):
    return render(request, 'user_list.html')
