from django.db import models
from datetime import datetime, timedelta
import cloudinary.models
class EventDay(models.Model):
    """
    Represents a single day of events.
    """
    title = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.date})"


class Speaker(models.Model):
    """
    Represents a speaker.
    Can be linked to multiple events.
    """
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, blank=True)
    organization = models.CharField(max_length=255, blank=True)
    photo = cloudinary.models.CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    """
    Represents an event on a specific EventDay.
    """
    day = models.ForeignKey(EventDay, related_name="events", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.CharField(max_length=50, blank=True)  # Auto-calculated
    forum = models.CharField(max_length=255, blank=True)
    speakers = models.ManyToManyField(Speaker, related_name="events", blank=True)

    def save(self, *args, **kwargs):
        """
        Auto-calculate duration based on start_time and end_time.
        Handles events crossing midnight.
        """
        if self.start_time and self.end_time:
            start = datetime.combine(datetime.today(), self.start_time)
            end = datetime.combine(datetime.today(), self.end_time)

            # Handle events crossing midnight
            if end < start:
                end += timedelta(days=1)

            diff = end - start
            total_minutes = diff.seconds // 60
            hours = total_minutes // 60
            minutes = total_minutes % 60

            if hours and minutes:
                self.duration = f"{hours} Hour {minutes} Min"
            elif hours:
                self.duration = f"{hours} Hour"
            else:
                self.duration = f"{minutes} Min"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.start_time} - {self.end_time})"
