# Create your views here.
from django.http import HttpResponse
from wine.models import brand
from wine.models import knowledge


def ShowBrand(request):
    recordTemplate = "{'title': '%s', 'date': '%s', 'content': '%s'}"
    recordList = '['
    for b in brand.objects.all():
        recordList += (recordTemplate % (b.title, b.date, b.content))
        recordList += ','
    recordList = recordList[0:-1] + ']'
    return HttpResponse(recordList)


def ShowKnowledge(request):
    recordTemplate = "{'title': '%s', 'date': '%s', 'content': '%s'}"
    recordList = '['
    for k in knowledge.objects.all():
        recordList += (recordTemplate % (k.title, k.date, k.content))
        recordList += ','
    recordList = recordList[0:-1] + ']'
    return HttpResponse(recordList)
