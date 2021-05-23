from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.

fake_info = [
    {
        'author': 'Mofiz Bhai',
        'content': 'HALA TORE CHUDI',
    },
    {
        'author': 'akij bhai',
        'content': 'AKIJ BIRI ZINDABAAD',
    }
]


def home(request, *args, **kwargs):
    context = {
    'post': fake_info,
    'title': 'Home',
    }
    return render(request, 'mainapp/home.html', context)


def about(request, *args, **kwargs):
    context = {
        'title': 'About',
    }
    return render(request, 'mainapp/about.html', context)


def messaging(request, *args, **kwargs):
    obj = Post.objects.get(id=1)
    if request.POST.get('msg_content') is not None and request.POST.get('msg_content') != '':       
        new_msg = request.POST.get('msg_content')
        obj.msg_content = new_msg
        obj.save()
    context = {
        'title': 'MSG',
        'content': obj.msg_content,
        
    }
    return render(request, 'mainapp/messaging.html', context)
