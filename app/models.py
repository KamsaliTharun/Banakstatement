from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('PREMIUM', 'Premium'),
        ('NON_PREMIUM', 'Non-Premium'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = (
        ('SEND', 'Send'),
        ('RECEIVE', 'Receive'),
        ('REQUEST', 'Request'),
    )
    sender = models.ForeignKey(User, related_name='sender_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver_transactions', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    fee = models.DecimalField(max_digits=15, decimal_places=2)
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class TransactionFee(models.Model):
    MIN_AMOUNT = 1000
    MAX_AMOUNT = 1000000
    MIN_FEE = 10
    MAX_FEE = 500
    transaction_type = models.CharField(max_length=20, choices=Transaction.TRANSACTION_TYPE_CHOICES, unique=True)
    min_amount = models.DecimalField(max_digits=15, decimal_places=2, default=MIN_AMOUNT)
    max_amount = models.DecimalField(max_digits=15, decimal_places=2, default=MAX_AMOUNT)
    min_fee = models.DecimalField(max_digits=15, decimal_places=2, default=MIN_FEE)
    max_fee = models.DecimalField(max_digits=15, decimal_places=2, default=MAX_FEE)


class SuperUser(models.Model):
    wallet = models.OneToOneField(Wallet, on_delete=models.CASCADE)
