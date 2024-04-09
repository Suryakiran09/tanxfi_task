from django.urls import path
from .views import *


urlpatterns = [
    path('create/', CreateOrderView.as_view(), name='create-order'),
    path('cancel/<int:order_id>/', CancelOrderView.as_view(), name='cancel-order'),
]