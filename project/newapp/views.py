from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


from django.http import HttpResponse

def home(abc):
    return HttpResponse('hello welcome to homepage')

def login(request):
    return HttpResponse('hello welcome to loginpage')                               