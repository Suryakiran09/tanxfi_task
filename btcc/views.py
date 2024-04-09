from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

class DepositView(APIView):
    def post(self, request):
        serializer = DepositSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        wallet = validated_data['wallet']
        amount = validated_data['amount']

        balance = Wallet.credit(cls=Wallet, sender=request.user, coin=wallet, amount=amount)
    
        message =  {
            "status" : "success",
            "message": "Wallet credited successfully",
            "payload" : {
                "balance" : balance,
                "currency": wallet
            }
        }
        return Response(message, status=201)
    
class WithDrawlView(APIView):
    def post(self, request):
        serializer = DepositSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        validated_data = serializer.validated_data
        
        wallet = validated_data['wallet']
        amount = validated_data['amount']

        balance = Wallet.withdrawl(cls=Wallet, sender=request.user, coin=wallet, amount=amount)
    
        message =  {
            "status" : "success",
            "message": "Wallet credited successfully",
            "payload" : {
                "balance" : balance,
                "transaction" : amount,
                "currency": wallet
            }
        }
        return Response(message, status=201)
    
class BalanceView(APIView):
    def get(self, request):
        queryset = Wallet.objects.filter(user = request.user)
        serializer = WalletSerializer(queryset, many=True)
        data = serializer.data
        message = {
            "status": "success",
            "msg" : "successfully fetched funds",
            "payload" : data
        }
        return Response(data = message, status = 200)    

