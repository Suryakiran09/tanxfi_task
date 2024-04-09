# tanfi_task/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('btc.urls')),
    path('user/', include('users.urls')),
    path('wallets/', include('btcc.urls')),
    path('orders/', include('orders.urls'),),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
