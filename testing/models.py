from django.db import models

# Create your models here.

class Reminder(models.Model):
    Title = models.CharField(max_length=200)
    Task = models.TextField(max_length=1000)
    Due_Date = models.DateTimeField(blank=True)
    
    class Meta:
        ordering = ['Due_Date']

# Create your models here.
