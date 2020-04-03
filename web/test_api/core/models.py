from django.db import models
from django.utils.crypto import get_random_string


class AppModel(models.Model):
    APP_ID = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    API_KEY = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def generate_api_key(self):
        api_key = get_random_string(length=32)
        self.API_KEY = api_key
        return api_key

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.API_KEY:
            self.generate_api_key()
        super().save()

