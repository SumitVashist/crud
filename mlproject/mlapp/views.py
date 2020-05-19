from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def datetimeinfo(request):
    now=datetime.datetime.now()
    h=int(now.strftime("%H"))
    m1='<h1>hello learner very very '
    if h<12:
        m1=m1+'Good Morning'
    elif h<16:
        m1=m1+'Good afternoon'
    elif h<21:
        m1=m1+'Good evening'
    else:
        m1=m1+'Good night'

    m1=m1+'</h1>'
    return HttpResponse(m1)


def supervised(request):
    now=datetime.datetime.now()
    h=int(now.strftime("%H"))
    m1='<h1>hello learner very very '
    if h<12:
        m1=m1+'Good Morning'
    elif h<16:
        m1=m1+'Good afternoon'
    elif h<21:
        m1=m1+'Good evening'
    else:
        m1=m1+'Good night'

    m1=m1+'</h1>'
    m1=m1+'<h1>Supervised learning</h1> '
    return HttpResponse(m1)


def unsupervised(request):
    msg='<h1>Unsupervised learning</h1> '
    return HttpResponse(msg)


def semisupervised(request):
    msg='<h1>semisupervised learning</h1> '
    return HttpResponse(msg)
