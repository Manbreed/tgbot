from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request: WSGIRequest):
    return 'login.html', {
        'message': 'MY_TODO_APP',
    }
