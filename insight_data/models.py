from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50)
    playback_id = models.CharField(max_length=100, default="")
    playback_time_instant = models.FloatField(default=0)
    video_url = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name