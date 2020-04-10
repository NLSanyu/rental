import uuid
from django.db import models
# import user model

class Estate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    location = models.TextField(max_length=100)
    description = models.TextField(max_length=255)
    # owner

    def __str__(self):
        return self.name

class Unit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    area = models.FloatField(default=0)
    price = models.CharField(max_length=30)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']