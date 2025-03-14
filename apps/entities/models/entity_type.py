from django.db import models
from django.utils.text import slugify

class EntityType(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Ej: "Peluquería"
    slug = models.SlugField(unique=True, blank=True)     # Ej: "peluqueria"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name