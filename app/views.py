from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    tn=input('enter a name')
    topics=Topic.objects.all()
    d={'topics':topics}
    TO=Topic.objects.get_or_create(Topic_name=tn)
    if TO[1]:
        return render(request,'display_topic.html',d)
        #return HttpResponse('Topic is created')
    else:
        return HttpResponse('data is already exits')

def insert_webpage(request):
    tn=input('enter a name')
    n=input('enter name')
    u=input('enter name')
    e=input('enter name')
    wps=Webpage.objects.all()
    d={'webpages':wps}
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    WO=Webpage.objects.get_or_create(Topic_name=TO,name=n,url=u,email=e)
    if WO[1]:
        return render(request,'display_webpage.html',d)
        #return HttpResponse('Webpage is created')
    else:
        return HttpResponse('data is already exits')

def insert_accessrecord(request):
    tn=input('enter a name')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    a=input('enter author')
    d=input('enter date')
    d={'access':AccessRecord.objects.all()}
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    WO=Webpage.objects.get_or_create(Topic_name=TO,name=n,url=u,email=e)[0]
    AR=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)
    if AR[1]:
        return render(request,'display_AR.html',d)
        #return HttpResponse('Accessrecord is created')
    else:
        return HttpResponse('data is already existed')


def insert_wp(request):
    tn=input('enter name')
    a=input('enter name')
    b=input('enter url')
    c=input('enter email')
    TOBJ=Topic.objects.filter(Topic_name=tn)
    d={}
    if TOBJ:
        TO=TOBJ[0]
        Webpage.objects.get_or_create(Topic_name=TO,name=a,url=b,email=c)
        return HttpResponse('topic is created')
    else:
        return HttpResponse('data is not available')
    

def display_topic(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    d={'webpages':Webpage.objects.all()}
    return render(request,'display_webpage.html',d)

def display_AR(request):
    d={'access':AccessRecord.objects.all()}
    return render(request,'display_AR.html',d)