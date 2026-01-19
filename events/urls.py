from django.urls import path
from .views import event_schedule

urlpatterns = [
    path('schedule/', event_schedule, name='event_schedule'),
]
