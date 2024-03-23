from django.shortcuts import render
from .models import Event
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def events(request):
    template=loader.get_template('events.html')
    events=Event.objects.all()
    context={
        'events': events
    }
    return HttpResponse(template.render(context,request))
def details(request,id):
    template=loader.get_template('details.html')
    event=Event.objects.get(id=id)
    context={
        'event': event
    }
    return HttpResponse(template.render(context,request))
