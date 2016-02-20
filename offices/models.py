from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name
