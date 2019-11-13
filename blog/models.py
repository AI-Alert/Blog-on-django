from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    post_author = models.CharField(max_length=200, default='')
    post = models.TextField()
    title = models.CharField(max_length=200)
    scheduled_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    def publish(self):
        self.scheduled_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title