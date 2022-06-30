from django.db import models

# Create your models here.
class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='collection_images/', blank=True)
    color = models.CharField(max_length=100, default='#ffffff')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Events(models.Model):
    collection_id = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='events_images/', blank=True)
    event_at = models.DateTimeField()
    def __str__(self):
        return self.title
class Articles(models.Model):
    collection_id = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='articles_images/', blank=True)
    def __str__(self):
        return self.title