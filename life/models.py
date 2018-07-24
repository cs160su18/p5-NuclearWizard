from django.db import models

#   class Event_List(models.Model):
#   name = models.CharField(max_length=100)
#   description = models.CharField(max_length=200)
  
class Event(models.Model):
  parent_event = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=200)
  
class Outcome(models.Model):
  parent_event = models.ForeignKey(Event, on_delete=models.CASCADE)
  narration = models.CharField(max_length=800)  

#   class Sub_Event(models.Model):
#   event = models.ForeignKey(Event, on_delete=models.CASCADE)
#   name = models.CharField(max_length=100)
#   description = models.CharField(max_length=200)
#   outcome = models.IntegerField(default=0)
  
### Goofing around with models ###
# Tables correspond to a final outcome for some event. An attack hits, a skill check succeeds, etc.
# The Tables will then be the parent to many descriptive narrations for that given outcome.
# class Table(models.Model):
#   # Each table will have a parent event.
#   parent_event = models.ForeignKey(Event, on_delete=models.CASCADE)
#   # Each table will have a name, typically the name of the outcome, like Hit, Miss, or Crit.
#   name = models.CharField(max_length=100)
  
