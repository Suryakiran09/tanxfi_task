# btc/models.py
from django.db import models

class PriceAlert(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('deleted', 'Deleted'),
        ('triggered', 'Triggered'),
    ]

    cryptocurrency = models.CharField(max_length=50)
    target_price = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')
