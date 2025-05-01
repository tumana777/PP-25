from django.db import models

class BaseManager(models.Manager):
    def get_expensive_products(self):
        return self.get_queryset().filter(price__gt=3000)