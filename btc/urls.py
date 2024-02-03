# btc/urls.py
from django.urls import path
from .views import PriceAlertListCreateView, PriceAlertDeleteView, PriceAlertStatusListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('alerts/create/', PriceAlertListCreateView.as_view(), name='price-alert-create'),
    path('alerts/delete/<int:pk>/', PriceAlertDeleteView.as_view(), name='price-alert-delete'),
    path('alerts/list/', PriceAlertStatusListView.as_view(), name='price-alert-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
