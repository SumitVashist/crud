# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView,DetailView
from testapp.models import Book
# Create your views here.


class BookListView(ListView):
    model=Book
    #template_name='template/books.html'
    #context_object_name='list_of_books'

class BookDetailView(DetailView):
    model=Book
    #defaultt
