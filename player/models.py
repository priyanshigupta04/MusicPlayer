from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='songs/')
    
    def __str__(self):
        return f"{self.title} - {self.artist}"