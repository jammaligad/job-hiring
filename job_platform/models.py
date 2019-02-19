from django.db import models
from datetime import datetime
# Create your models here.

class Job(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/images', blank=True, null=True)

    def __str__(self):
        return '{} at {}'.format(self.position,self.company)

class Post(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name = "posts",blank=True, null=True)
    date_created = models.DateTimeField(default=datetime.now())
    date_modified = models.DateTimeField(default=datetime.now(),blank=True,null=True)


class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name = "applications",blank=True, null=True)
    date_created = models.DateTimeField(default=datetime.now())
    date_modified = models.DateTimeField(default=datetime.now(),blank=True,null=True)
