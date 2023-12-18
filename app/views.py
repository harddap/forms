from django.http import HttpResponse
from django.shortcuts import render

from .froms import *


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Noname')
        age = request.POST.get('age', 'zero')
        agree = request.POST.get
        return HttpResponse(f'Пользователь - {name}, возраст - {age}, {agree}')
    else:
        form = UserForm()
        return render(request, 'app/index.html', context={'form': form})


def appointmentForm(request):
    return render(request, 'app/appointment.html')

# def postuser(request):
#     name = request.POST.get('name', 'Noname')
#     age = request.POST.get('age', 'zero')
#     return HttpResponse(f'Пользователь - {name}, возраст - {age}')
    # return HttpResponse(f'{name}, {email}, {phone}, {select_service}, {comments}')

def info(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    select_service = request.POST.get('select_service')
    comments = request.POST.get('order_textarea')
    info_form = Appointform()
    return HttpResponse(f'{name}, {email}, {phone}, {select_service}, {comments}', context={'info_form': info_form})

def news(request):
    if request.method == 'POST':
        return HttpResponse('New news')
    else:
        form = NewsForm()
        return render(request, 'app/news.html', context={'form': form})
