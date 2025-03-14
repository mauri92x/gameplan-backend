
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_entity_owner = models.BooleanField(default=False)  # Indica si es propietario de una entidad
    phone = models.CharField(max_length=15, blank=True)  # Opcional para WhatsApp

    def __str__(self):
        return self.username