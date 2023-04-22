from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFOD=TopicForm(request.POST)
        if TFOD.is_valid():
            TFOD.save()
            return HttpResponse('topic insertion is completed successfully')

    
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}

    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('webpage insertion is done successfully')
    return render(request,'insert_webpage.html',d)


def insert_AccessRecord(request):
    AFO=AccessForm()
    d={'AFO':AFO}

    if request.method=='POST':
        AFDO=AccessForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('AccessRecord insertion is done successfully')
    return render(request,'insert_AccessRecord.html',)