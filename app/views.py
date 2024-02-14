from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
from app.forms import *
def topic(request):
    ENTF=Topic_forms()
    d={'ENTF':ENTF}
    if request.method=='POST':
        DNTF=Topic_forms(request.POST)
        if DNTF.is_valid():
            tn=DNTF.cleaned_data['tname']
            TO=Topic.objects.get_or_create(tname=tn)[0]
            TO.save()
            return HttpResponse('Topic is created......!')
        else:
            return HttpResponse('Topic is not valid.....!')
    return render(request,'topic_forms.html',d)

def webpage(request):
    ENWF=Webpage_forms()
    d={'ENWF':ENWF}
    if request.method=='POST':
        DNWF=Webpage_forms(request.POST)
        if DNWF.is_valid():
            tn=DNWF.cleaned_data['tname']
            na=DNWF.cleaned_data['name']
            em=DNWF.cleaned_data['email']
            ur=DNWF.cleaned_data['url']
            TO=Topic.objects.get(tname=tn)
            WO=Webpage.objects.get_or_create(tname=TO,name=na,email=em,url=ur)[0]
            WO.save()
            return HttpResponse('webpage is created...')
        else:
            return HttpResponse('webpage is not valid..')
    return render(request,'webpage_forms.html',d)

def access_record(request):
    ENAF=Accessrecord_forms()
    d={'ENAF':ENAF}
    if request.method=='POST':
        DNAF=Accessrecord_forms(request.POST)
        if DNAF.is_valid():
            na=DNAF.cleaned_data['name']
            au=DNAF.cleaned_data['author']
            da=DNAF.cleaned_data['date']
            WO=Webpage.objects.get(pk=na)
            AO=Accessrecord.objects.get_or_create(name=WO,author=au,date=da)[0]
            AO.save()
            return HttpResponse('accessrecord is created.....')
        else:
            return HttpResponse('accessrecord is not valid.....!')
    return render(request,'accessrecord_forms.html',d)
