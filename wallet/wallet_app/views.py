from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response
from wallet_app.serializers import IntializeWalletSerializer, WalletSerializer
from wallet_app import services

class InitializeWallet(APIView):
    serializer_class = IntializeWalletSerializer
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            return services.initialize_wallet(serializer.validated_data['customer_xid'])
        else:
            return Response(serializer.errors)

class EnableWallet(APIView):
    serializer_class = WalletSerializer

