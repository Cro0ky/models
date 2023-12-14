from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from .models import *


def posts(request):
    post = Posts.objects.all()
    return render(request, 'app/forum.html', context={'post': post})


def data(request):
    tom = User.objects.get_or_create(name='Tom', age=14)

    try:
        mike = User.objects.get(name='Mike')
        mike.delete()
    except:
        mike = User(name='Mike', age=21, url='https://cdn-icons-png.flaticon.com/512/858/858962.png')
        mike.save()

    data = User.objects.all()[:2]
    return render(request, 'app/data.html', context={'data': data})


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            return HttpResponse(
                f'<h1>{name}, поздравляю с регистрацией! <br>Данные: name - {name}, password - {password}, Email - {email}</h1>')
        else:
            return HttpResponse('Данные не валидны')
    else:
        form = UserForm()
        return render(request, 'app/index.html', context={'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            if name == 'User1' and password == '12345678':
                return HttpResponse(f'<h1>Поздравляю с успешным входом {name}! </h1>')
            else:
                return redirect("home")
        else:
            return HttpResponse('Данные не валидны')
    else:
        form = UserLoginForm()
        return render(request, 'app/LogIn.html', context={'form': form})
