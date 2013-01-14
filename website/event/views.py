# Create your views here.
from django.shortcuts import render
from event.models import Event, EventForm

# Basic view to return just html
def home(request):
    return render(request, 'index.html')

# View to return all events
def all_events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events, 'form': EventForm()})

def post_event(request):
    pass
