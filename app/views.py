from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def create_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse(str(TFDO.cleaned_data))
        else:
            return HttpResponse('Data is invalid')

    return render(request,'create_topic.html',context=d)

def create_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
            WO.save()
            return HttpResponse(str(WFDO.cleaned_data))
        else:
            return HttpResponse('Data is invalid')

    return render(request,'create_webpage.html',context=d)


def create_accessrecord(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            n=AFDO.cleaned_data['name']
            WO=Webpage.objects.get(pk=n)
            a=AFDO.cleaned_data['author']
            d=AFDO.cleaned_data['date']
            AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
            AO.save()
            return HttpResponse(str(AFDO.cleaned_data))

        else:
            return HttpResponse('Invalid Data')
     
    return render(request,'create_accessrecord.html',context=d)
