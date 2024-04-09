from django.urls import path
from .views import *


urlpatterns = [
    path('deposit/', DepositView.as_view(), name='deposit'),
    path('withdrawl/', WithDrawlView.as_view(), name='withdraw'),
    path('balances/', BalanceView.as_view(), name='balances'),
]