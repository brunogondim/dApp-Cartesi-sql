from django.db import models

# Create your models here.

class inputs(models.Model):
    payload = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name