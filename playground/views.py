from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def calculateX():
    x = 10
    return x


def say_hello(request):
    x = calculateX()
    print(x)
    return render(request, 'hello.html', {
        'name': 'Usman'
    })
