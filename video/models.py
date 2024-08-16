from django.db import models
from datetime import date

class Video(models.Model):
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=100)
    is_new = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='videos/thumbs', blank=True, null=True)
    video_file = models.FileField(upload_to='videos', blank=True, null=True)
    
    def __str__(self):
        return f'({self.id}) {self.title}'