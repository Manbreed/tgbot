from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request: WSGIRequest):
    request_data_dict = dict(request.GET.items())

    a = request_data_dict['var_a']
    b = request_data_dict['var_b']
    name = request_data_dict['name']
    age = request_data_dict['age']

    return render(
        request,
        'index.html',
        {
            'result': int(a) * int(b),
            'name': name,
            'age': age,
        }
    )
    #return render(request, 'index.html')
