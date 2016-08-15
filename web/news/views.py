from django.shortcuts import render, get_object_or_404
from news.models import Post
from news.models import Link
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

def index(request):
        posts = Post.objects.filter(published=True)
        return render(request, 'news/index.html', {'posts': posts})

def schedule(request):
        return render(request, 'news/schedule.html')

def links(request):
        links  = Link.objects.filter(published=True)
        return render(request, 'news/links.html', {'links': links})

def subscribe(request):
        return render(request, 'news/subscribe.html')

def competition(request):
        return render(request, 'news/competition.html')

def rules(request):
        return render(request, 'news/rules.html')
