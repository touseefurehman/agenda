from django.shortcuts import render
from .models import EventDay

def event_schedule(request):
    days = EventDay.objects.prefetch_related('events__speakers').all()
    return render(request, 'events/schedule.html', {'days': days})
