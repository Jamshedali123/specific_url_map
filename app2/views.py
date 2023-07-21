from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('this is app2 suffix first')

def second(request):
    return HttpResponse('this is app2 suffix second')
