from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=500)
    details = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
