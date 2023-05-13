from djongo import models as mongo_models
from django.db import models


class Log(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    message = mongo_models.TextField(max_length=1000)

    created_at = mongo_models.DateTimeField(auto_now_add=True)
    updated_at = mongo_models.DateTimeField(auto_now=True)

    class Meta:
        _use_db = 'nonrel'
        ordering = ("-created_at",)

    def __str__(self):
        return self.message


class Post(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField

    def __str__(self):
        return self.title
