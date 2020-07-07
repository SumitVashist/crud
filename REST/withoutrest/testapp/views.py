from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
# Create your views here.

def emp_data_view(request):
    emp_data={
    'eno':100,
    'ename':'Sumit',
    'esal':100000,

    }
    resp='<h1>Employee Number : {}<br> Employee Name : {}<br> Employee Salary : {} </h1> '.format(emp_data['eno'],emp_data['ename'],
    emp_data['esal'])

    return HttpResponse(resp)

def emp_data_jsonview(request):
    emp_data={
    'eno':100,
    'ename':'Sumit',
    'esal':100000,

    }
    json_data=json.dumps(emp_data)

    return HttpResponse(json_data,content_type='application/json')


def emp_data_jsonview2(request):
    emp_data={
    'eno':100,
    'ename':'Sumit',
    'esal':100000,

    }
    return JsonResponse(emp_data)
