from django.db import models
from django.utils import timezone

# Create your models here.


class Tweet(models.Model):
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    datetime = models.DateTimeField(
        'datetime', default=timezone.now, null=False, blank=False)
