from django.db import models
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    displaypic = models.ImageField(upload_to='profilepics/', null=True, blank=True, default='profilepics/default_profilepic.png')
    company = models.CharField(max_length=100, default='N/A')
    about = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    resume = models.FileField(upload_to='resume/', null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True, default='images/default_thumbnail.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='recruiter')
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    archived = models.BooleanField(default=False, editable=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp", "-updated"]

class Application(models.Model):
    jobpost = models.ForeignKey(JobPost, on_delete=models.CASCADE, editable=False, related_name='post', blank=True, null=True)
    applicant = models.ForeignKey(User, editable=False, on_delete=models.CASCADE, related_name='recruits')
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_applied = models.DateTimeField(auto_now=False, auto_now_add=True)
    archived = models.BooleanField(default=False, editable=False)

    class Meta:
        ordering = ["-date_applied", "-updated"]

