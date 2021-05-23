from django.db import models

# Create your models here.
class Post(models.Model):
    msg_content = models.TextField(blank=True, null=True)