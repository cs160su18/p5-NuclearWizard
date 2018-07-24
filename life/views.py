from django.shortcuts import render
from django.core import serializers
from life.models import *
from django.core.serializers import serialize

def events(request):
  
  if request.method == "POST":
    print(json.loads(request.body))
    return HttpResponse("")
  
  else:
    all_events = Event.objects.all()
    response = serialize("json", all_events)
    return HttpResponse(response, content_type="application/json")

def outcomes(request):
  
  if request.method == "POST":
    print(json.loads(request.body))
    return HttpResponse("")
  
  else:
    all_outcomes = Outcome.objects.all()
    response = serialize("json", all_outcomes)
    return HttpResponse(response, content_type="application/json")
  
def index(request):
  all_events = Event.objects.all()
  all_outcomes = Outcome.objects.all()
  return render(request, 'life/index.html', {"events": all_events, "outcomes": all_outcomes})