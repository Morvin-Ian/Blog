from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    caption = models.CharField(max_length=100)
    body = models.TextField()
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption


