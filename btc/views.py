# btc/views.py
from django.core.cache import cache
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import PriceAlert
from .serializers import PriceAlertSerializer

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class PriceAlertListCreateView(generics.ListCreateAPIView):
    serializer_class = PriceAlertSerializer

    def get_queryset(self):
         return PriceAlert.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class PriceAlertDeleteView(generics.DestroyAPIView):
    queryset = PriceAlert.objects.all()
    serializer_class = PriceAlertSerializer

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class PriceAlertStatusListView(generics.ListAPIView):
    serializer_class = PriceAlertSerializer

    def get_queryset(self):
        status_filter = self.request.query_params.get('status', None)
        if status_filter:
             return PriceAlert.objects.all(status=status_filter)
        else:
             return PriceAlert.objects.all()