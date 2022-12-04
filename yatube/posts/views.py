from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'posts/index.html'
    context = {
        'text': 'Это главная страница проекта Yatube.',
    }   
    return render(request, template, context) 


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request):
    template = 'posts/group_posts.html'
    # Словарь с данными принято называть context
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube',
    }   
    return render(request, template, context) 

# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template) 