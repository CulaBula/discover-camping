from django.db import models
from django.utils import timezone

class Park(models.Model):
    park_name = models.CharField(max_length=100)
    park_type = models.CharField(max_length=100)
    park_status = models.CharField(max_length=100)
    date_updated = models.DateField(default=timezone.now)