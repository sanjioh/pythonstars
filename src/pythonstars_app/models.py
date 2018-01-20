# coding: utf-8
from django.db import models


class DataPoint(models.Model):
    author = models.CharField(max_length=1024)
    repository = models.CharField(max_length=1024)
    stars = models.PositiveIntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)
