# models.py

from django.db import models

class Auto(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} ({self.color})"
