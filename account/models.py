from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ACCOUNTS = (
    ('Savings', 'Savings'),
    ('Current', 'Current'),
)
GENDERS = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class UserBankAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50, choices = ACCOUNTS )
    account_number = models.IntegerField(unique = True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices = GENDERS)
    initial_account_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=True)

    def __str__(self):
        return str(self.account_number)

class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name = 'address', on_delete=models.CASCADE )
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length= 100)
    poster_code = models.IntegerField()
    country = models.CharField(max_length=120)
    
    def __str__(self):
        return str(self.user.account.account_number)