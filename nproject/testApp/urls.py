from django.urls import path
from testApp import views
urlpatterns = [

    path('date/', views.dateinfo),

]
