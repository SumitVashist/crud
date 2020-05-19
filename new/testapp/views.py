from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def welcome(request):

    s='<h1>Hello WELCOME</h1><hr>'
    return HttpResponse(s)

def timeinfo(request):
    date=datetime.datetime.now()
    msg='<h1>hello </h1><hr>'
    msg=msg+'<h1>Now server time is: '+str(date)+'</h1>'
    return HttpResponse(msg)
