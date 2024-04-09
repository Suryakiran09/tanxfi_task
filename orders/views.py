from django.shortcuts import render
from rest_framework.decorators import APIView
from decimal import Decimal
from .serializers import *
from rest_framework.response import Response
from .models import *
from btcc.models import *
from rest_framework import status
from django.db.models import Sum

import ccxt

def get_real_time_price(symbol):
    kraken = ccxt.kraken()
    ticker = kraken.fetch_ticker(symbol)
    return ticker['last']


class CreateOrderView(APIView):

    def post(self, request):
        user = request.user
        data = request.data
        print(data)
        sell_currency = data.get('sell_currency')
        buy_currency = data.get('buy_currency')
        amount = Decimal(data.get('amount'))
        side = data.get('side')

        symbol = f"{sell_currency}/{buy_currency}"
        real_time_price = get_real_time_price(symbol)

        wallet = Wallet.objects.get(user=user, wallet=sell_currency)
        
        available_balance = wallet.balance - wallet.locked_balance
        
        if wallet.balance < amount:
            return Response({'error': 'Insufficient funds in your wallet.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if available_balance < amount:
            return Response({'error': 'You have insufficient balance and Even if it is there you are trying to use locked balance'}, status=status.HTTP_400_BAD_REQUEST)

        buy_amount = amount * Decimal(real_time_price)

        order = Order.objects.create(
            user=user,
            sell_currency=sell_currency,
            buy_currency=buy_currency,
            amount=amount,
            side=side,
            price=buy_amount
        )
        
        wallet.locked_balance += amount
        wallet.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CancelOrderView(APIView):
    def post(self, request, order_id):
        order = Order.objects.get(id=order_id, user=request.user, state='pending')
        if not order:
            return Response({'error': 'Order not found or already processed.'}, status=status.HTTP_404_NOT_FOUND)

        order.state = 'cancelled'
        order.save()

        message = {
            "Status": "success",
            "Message": "Successfully cancelled.",
            "Paylaod": {}
        }

        return Response(message, status=status.HTTP_200_OK)