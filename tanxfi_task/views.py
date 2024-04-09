from django.db.models import Sum, Q
from datetime import datetime
from rest_framework.decorators import APIView
from orders.models import Order
from rest_framework.response import Response
from rest_framework import status

class DashboardView(APIView):
    def get(self, request):
        from_time = request.GET.get('from_time')
        to_time = request.GET.get('to_time')

        if from_time and to_time:
            from_time = datetime.fromparsisec(from_time)
            to_time = datetime.fromparsisec(to_time)
            orders = Order.objects.filter(
                created_at__range=(from_time, to_time)
            ).values('sell_currency').annotate(volume=Sum('amount'))
        else:
            orders = Order.objects.values('sell_currency').annotate(volume=Sum('amount'))

        data = {order['sell_currency'].lower(): order['volume'] for order in orders}

        message = {
            "status": "success",
            "message": "Data fetched successfully",
            "payload": data
        }

        return Response(message, status=status.HTTP_200_OK)