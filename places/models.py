from django.db import models

class Regions(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Regions'
        verbose_name_plural = "Regions"
    
    def __str__(self):
        return self.name