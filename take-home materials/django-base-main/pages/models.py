from django.db import models

class Event(models.Model):
    event_date = models.DateField()
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    additional_info_link = models.URLField()

    def _str_(self):
        return self.event_name

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def _str_(self):
        return self.name

class EventTag(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.event.event_name} - {self.tag.name}"
