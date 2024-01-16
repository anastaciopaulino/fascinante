from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f'{self.name}'