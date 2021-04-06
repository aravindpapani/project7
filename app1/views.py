from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>Welcome to index of App1</h1>")

def carry_data(request,data):
    return HttpResponse(f'<h1>The Recieved data is {data}</h1>')

def facto(request,num):
    fact = 1
    for i in range(1,int(num)+1):
        fact = fact*i
    return HttpResponse(f'<h1>The Factorial of {num} is {fact}</h1>')

def add(request,num1,num2):
    try:
        num1=int(num1)
    except:
        num1=float(num1)
    try:
        num2=int(num2)
    except:
        num2=float(num2)
    return HttpResponse(num1+num2)
def Sub(request,num1,num2):
    try:
        num1 = int(num1)
    except:
        num1=float(num1)
    try:
        num2 = int(num2)
    except:
        num2=float(num2)
    return HttpResponse(num1-num2)