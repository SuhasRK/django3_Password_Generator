from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'Password_Gen/home.html',{'name':'Suhas RK'})

def password(request):
    char=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
       char.extend(list('!@#$%^&*()_+{:"|<>?1234567890'))
    password=''
    for i in range(length):
        password+=random.choice(char)

    return render(request,'Password_Gen/password.html',{'gen_pass':password})

def about(request):
    return render(request,'Password_Gen/about.html')
