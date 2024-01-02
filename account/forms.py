from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserBankAccount, UserAddress

ACCOUNTS = (
    ('Savings', 'Savings'),
    ('Current', 'Current'),
)
GENDERS = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class UserRegisterFrom (UserCreationForm):
    account_type = forms.ChoiceField( choices = ACCOUNTS )
    birth_date = forms.DateField(widget= forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField( choices = GENDERS)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    poster_code = forms.IntegerField()
    country = forms.CharField(max_length=120)
    
    class Meta:
        model = User
        fields = ['username', 'account_type', 'first_name', 'last_name', 'email', 'birth_date','gender', 'street_address', 
                 'country', 'city', 'poster_code', 'password1', 'password2']
        
        def save(self, commit = True ):
            our_user = super().save(commit=False)
            if commit == True:
                our_user.save()
                account_type = self.clean_data.get('account_type')
                birth_date = self.clean_data.get('birth_date')
                gender = self.clean_data.get('gender')
                street_address = self.clean_data.get('street_address')
                city = self.clean_data.get('city')
                country = self.clean_data.get('country')
                poster_code = self.clean_data.get('poster_code')
                
                UserBankAccount.objects.create(
                    account_type = account_type,
                    account_number = 10000 + our_user.id,
                    birth_date = birth_date,
                    gender = gender,
                )
                
                UserAddress.objects.create(
                    street_address = street_address,
                    city = city,
                    country = country,
                    poster_code = poster_code,
                )
                
            return our_user
            