from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

class DocumentVersion(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    version = models.IntegerField()
    content = models.TextField()
    saved_at = models.DateTimeField(auto_now_add=True)
