from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


# method == 'POST' or method == 'GET'

def login_view(request: WSGIRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_page = request.GET.get('next')

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

        if next_page is not None:
            return redirect(next_page)

        return redirect('todo_main')



    return render(request, 'login.html')


# def __check_data_before_registration(request, username, password, password_confirm, email):
#     if password != password_confirm:
#         return render(request, 'registration.html', {
#             'error_message': 'Пароли не совпадают',
#         })
#     if User.objects.filter(username=username).exists():
#         return render(request, 'registration.html', {
#             'error_message': 'Пользователь с таким логином уже есть',
#         })
#     if User.objects.filter(email=email).exists():
#         return render(request, 'registration.html', {
#             'error_message': 'Пользователь с таким email уже есть',
#         })
#     if len(password) < 10:
#         return render(request, 'registration.html', {
#             'error_message': 'Пароль слишком короткий',
#         })

def registration(request: WSGIRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        email = request.POST['email']
        # return __check_data_before_registration(request, username, password, password_confirm, email)

        user = User.objects.filter(
            username=username,
            password=password,
            email=email,
        )
        if password != password_confirm:
            return render(request, 'registration.html', {
                'error_message': 'Пароли не совпадают',
            })
        if User.objects.filter(username=username).exists():
            return render(request, 'registration.html', {
                'error_message': 'Пользователь с таким логином уже есть',
            })
        if User.objects.filter(email=email).exists():
            return render(request, 'registration.html', {
                'error_message': 'Пользователь с таким email уже есть',
            })
        if len(password) < 10:
            return render(request, 'registration.html', {
                'error_message': 'Пароль слишком короткий',
            })
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'login.html', {
                'error_message': 'Некорректный емейл',
            })

        user = User()
        user.username = username
        user.password = password
        user.email = email
        try:
            user.save()
        except Exception as e:
            return render(request, 'registration.html', {
                'error_message': 'ServerError',
            })
            return render(request, 'info.html', {
                'error_message': 'Регистрация прошла успешно',
            })

        return render(request, 'registration.html')


def user_list(request: WSGIRequest):
    return render(request, 'user_list.html')
