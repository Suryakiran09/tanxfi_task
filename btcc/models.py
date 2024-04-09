from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.validators import ValidationError
from decimal import Decimal
# Create your models here.

CustomUser = get_user_model()

class Wallet(models.Model):
    choices = [
        ('BTC', 'BTC'),
        ('ETH', 'ETH'),
        ('DOGE', 'DOGE'),
        ('USDT', 'USDT')
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    wallet = models.CharField(choices=choices, max_length=10)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))
    locked_balance = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))
    
    @classmethod
    def credit(self, cls,sender, coin, amount):
        amount = Decimal(amount)
        wallets = Wallet.objects.filter(user = sender)
        coin = wallets.filter(wallet = coin).first()
        coin.balance =  (coin.balance.quantize(Decimal('.00')) + amount.quantize(Decimal('.00'))).quantize(Decimal('.00'))
        coin.save()
        
        return coin.balance
    
    @classmethod
    def withdrawl(self, cls, sender, coin , amount):
        amount = Decimal(str(amount))
        wallets = Wallet.objects.filter(user = sender)
        coin = wallets.filter(wallet = coin).first()
        if coin.balance < amount:
            raise ValidationError("Balance Insufficient")
        
        coin.balance =  (coin.balance.quantize(Decimal('.00')) - amount.quantize(Decimal('.00'))).quantize(Decimal('.00'))
        coin.save()
        
        return coin.balance

