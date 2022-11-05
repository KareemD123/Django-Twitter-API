from django.db import models

# Create your models here.

class Tweet(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.name}'s tweet says: {self.description}"









