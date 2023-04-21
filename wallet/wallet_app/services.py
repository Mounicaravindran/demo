from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Wallet, Customer
from rest_framework.authtoken.models import Token

def initialize_wallet(customer_xid):

    user = User.objects.create_user(customer_xid)
    customer = Customer.objects.create(user=user)
    wallet = Wallet.objects.create(owned_by=customer)
    token = Token.objects.create(user=user)
    print(token.key)
    response = {}
    response["data"] = {"token": token.key}
    response["status"] = "success"
    return Response(response)
