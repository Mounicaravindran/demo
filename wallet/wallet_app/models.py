from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True, db_column='customer_xid')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=255)


class Wallet(models.Model):
    id = models.AutoField(primary_key=True)
    activated = models.BooleanField(default=False)
    balance = models.FloatField(max_length=20, default=0)
    owned_by = models.OneToOneField(Customer, on_delete=models.DO_NOTHING)