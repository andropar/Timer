from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.
class Session(models.Model):
    duration = models.DurationField(default=timedelta)
    date = models.DateField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.user.username
