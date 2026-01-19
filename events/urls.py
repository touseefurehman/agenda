from django.urls import path
from .views import event_schedule

urlpatterns = [
    path('', event_schedule, name='event_schedule'),
]
