# Create your views here.
from django.shortcuts import render
from event.models import Event, EventForm
# for get_events function
import json
from django.http import HttpResponse, HttpResponseRedirect

# Basic view to return just html
def home(request):
    return render(request, 'index.html')

# View to return all events
def all_events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def get_events(request):
    events = [event.title for event in Event.objects.all()]
    return HttpResponse(json.dumps({'titles':events}), content_type="application/json")

def register(request):
    return render(request, 'register.html', {'form': EventForm()})

def post_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            e = Event(title = form.cleaned_data['title'],
                      date = form.cleaned_data['date'],
                      location = form.cleaned_data['location'],
                      description = form.cleaned_data['description'])
            e.save()

    return HttpResponseRedirect('/events/')
