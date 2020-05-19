# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def count_view(request):
    count=int(request.COOKIES.get('count',0))
    newcount=count+1
    response=render(request,'testapp/count.html',{'count':newcount})
    response.set_cookie('count',newcount,max_age=180)
    return response
