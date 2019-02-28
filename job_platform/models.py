from django.db import models
<<<<<<< HEAD
from datetime import datetime
from django.conf import settings
# Create your models here.

class Job(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)

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
=======
from django.contrib.auth.models import User

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='user')
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp", "-updated"]
>>>>>>> d057f28c8115c1d76ca936d9ab70d4b9837a7541
