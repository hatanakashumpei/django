from django.http.response import Http404
from django.shortcuts import render, resolve_url
from django.http  import HttpResponse

# Create your views here.

# Q1
def add(request, num1, num2):
    return HttpResponse(f'<h1>{num1 + num2}</h1>')

# Q2
def minus(request, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return HttpResponse(f'<h1>{num1 - num2}</h1>')

# Q3
def div(request, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return HttpResponse(f'<h1>{round(num1 / num2)}</h1>')
