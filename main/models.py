from django.db import models

# Create your models here.

class Subscribers(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} {self.email}'

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'