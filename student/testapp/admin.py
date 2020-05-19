# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from testapp.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']
# Register your models here.

admin.site.register(Student,StudentAdmin)
