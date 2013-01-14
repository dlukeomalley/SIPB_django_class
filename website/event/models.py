# standard import to get access to models.Model
from django.db import models
# to create a form from a model
from django.forms import ModelForm

class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __unicode__(self):
        return self.title

class EventForm(ModelForm):
    class Meta:
        model = Event
