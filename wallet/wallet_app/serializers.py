from rest_framework import serializers
from wallet_app.models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

class IntializeWalletSerializer(serializers.Serializer):
    customer_xid = serializers.CharField(max_length=60)