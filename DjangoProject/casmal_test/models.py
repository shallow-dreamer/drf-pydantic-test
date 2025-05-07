# models.py
from django.db import models

class Experiment(models.Model):
    name = models.CharField(max_length=100)
    config = models.JSONField()  # 用于存储嵌套参数（字典或列表）
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Dataset(models.Model):
    name = models.CharField(max_length=100)
    source_url = models.URLField()
    experiment = models.ForeignKey(Experiment, related_name="datasets", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
