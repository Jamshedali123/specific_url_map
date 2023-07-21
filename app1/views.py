from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>this is app1 and suffix first</h1>')

def second(request):
    return HttpResponse('<marquee><h1>this is app1 suffix second</h1></marquee>')

