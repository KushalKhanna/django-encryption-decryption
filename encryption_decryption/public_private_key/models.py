from django.db import models

# Create your models here.
class Messages(models.Model):
    message = models.BinaryField(max_length = 5000)
