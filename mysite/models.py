from django.db import models

# Create your models here.
class Post(models.Model):
    pid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

