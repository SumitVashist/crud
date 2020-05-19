from django.shortcuts import render
import datetime
# Create your views here.
def dateinfo(request):
    date=datetime.datetime.now()
    name="Sumit"
    my_dict={'msg':date,'guest':name}
    return render(request,'testApp/test.html',context=my_dict)
