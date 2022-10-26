from django.db import models
import uuid

class Artiste(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    date_released = models.DateField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
        
class Lyric(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
