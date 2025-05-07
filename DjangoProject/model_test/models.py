from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=100)


class Dataset(models.Model):
    name = models.CharField(max_length=100)
    source_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


class Experiment(models.Model):
    name = models.CharField(max_length=100)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    config = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
