from django.db import models
from django.contrib.auth.models import User

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True, default='images/default_thumbnail.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='recruiter')
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp", "-updated"]