from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=500)
    details = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    completed = models.BooleanField()

    def __str__(self):
        return self.title