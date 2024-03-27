# btc/tasks.py
from django.core.mail import send_mail
from django.conf import settings
import requests
from .models import PriceAlert
from celery import shared_task
from .serializers import PriceAlertSerializer
import json

@shared_task
def get_latest_cryptocurrency_price():
    api_url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=1&page=1&sparkline=false'
    
    response = requests.get(api_url)
    data = response.json()
    if response.status_code == 200 and data:
        return data[0]['current_price']
    else:
        return None

@shared_task
def check_price_and_notify_periodic():
    # Fetch all active alerts
    alerts = PriceAlert.objects.filter(status='created')

    for alert in alerts:
        latest_price = get_latest_cryptocurrency_price()
        
        if latest_price and latest_price <= alert.target_price:
            print("went into this")
            print(f'The price of {alert.cryptocurrency} has reached your target price of {alert.target_price}!')
            # Send email using Gmail SMTP
            subject = 'Price Alert Triggered'
            message = f'The price of {alert.cryptocurrency} has reached your target price of {alert.target_price}!'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['xyz@gmail.com']
            
            alert.status = 'triggered'
            alert.save()

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            