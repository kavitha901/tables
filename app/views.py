from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    tn=input('enter a name')
    TO=Topic.objects.get_or_create(Topic_name=tn)
    if TO[1]:
        return HttpResponse('Topic is created')
    else:
        return HttpResponse('data is already exits')
    
def insert_webpage(request):
    tn=input('enter a name')
    n=input('enter name')
    u=input('enter name')
    e=input('enter name')
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    WO=Webpage.objects.get_or_create(Topic_name=TO,name=n,url=u,email=e)
    if WO[1]:
        return HttpResponse('Webpage is created')
    else:
        return HttpResponse('data is already exits')

def insert_accessrecord(request):
    tn=input('enter a name')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    a=input('enter author')
    d=input('enter date')
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    WO=Webpage.objects.get_or_create(Topic_name=TO,name=n,url=u,email=e)[0]
    AR=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)
    if AR[1]:
        return HttpResponse('Accessrecord is created')
    else:
        return HttpResponse('data is already existed')
    