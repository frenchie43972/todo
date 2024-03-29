from django.db import models

class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  completed = models.BooleanField(default=False)
  created_date = models.DateTimeField(auto_now_add=True)
  completed_date = models.DateTimeField(null=True, blank=True)