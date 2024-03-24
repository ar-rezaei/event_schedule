from django.shortcuts import render
from .models import Event
from django.template import loader
from django.http import HttpResponse
# Create your views here.
from datetime import datetime,timezone

def events(request):
    template=loader.get_template('events.html')
    events=Event.objects.all()
    now=datetime.now(timezone.utc)
    for event in events :
        start=event.start
        duration = event.duration
        if start+duration <now:
            status='past'
        elif start < now :
            status='present'
        else:
            status='future'

        event.timestatus=status    
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
