from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    STATE_CHOICES = (
        ('pending', 'Pending'),
        ('canceled', 'Canceled'),
        ('success', 'Success'),
    )

    SIDE_CHOICES = (
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sell_currency = models.CharField(max_length=10)
    buy_currency = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    side = models.CharField(max_length=4, choices=SIDE_CHOICES)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)