from django.db import models
from apps.users.models import User 

class Entity(models.Model):
  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity_type = models.ForeignKey('EntityType', on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True)
    operating_hours = models.JSONField(default=dict)

    def __str__(self):
        return self.name