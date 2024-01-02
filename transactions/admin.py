from django.contrib import admin
from transactions.views import ConfarmationEmail

# from transactions.models import Transaction
from .models import Bankrupt, Transaction
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'balance_after_transaction', 'transaction_type', 'loan_approve']
    
    def save_model(self, request, obj, form, change):
        obj.account.balance += obj.amount
        obj.balance_after_transaction = obj.account.balance
        obj.account.save()
        super().save_model(request, obj, form, change)

        mail_subject = 'Loan_approve'        
        to_email = request.user.email
        ConfarmationEmail(request.user ,to_email, "Loan approve", mail_subject, obj.account.balance, 'transactions/loan_email.html')

admin.site.register(Bankrupt)