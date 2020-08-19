from django.shortcuts import render
from django.http import HttpResponse
import operator
def home(requests):
    return render(requests,'app1/home.html',{'username':'suji'})
def aboutus(requests):
    return render(requests,'app1/about.html',{'userId':'suji107'})
def myhobbies(requests):
    return HttpResponse('<h1>my hobbies are reading books,coding,listening music</h1>')
# Create your views here.
