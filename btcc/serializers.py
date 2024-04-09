from rest_framework import serializers

from .models import *

class DepositSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model= Wallet
        fields=['wallet', 'amount']

class WithDrawlSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model: Wallet
        fields=['wallet', 'amount']
            
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['balance', 'wallet']