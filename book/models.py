from django.db import models
from api.models import User

class Books(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    category = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return title
