from django.core import validators
from django import forms
from .models import Account
class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=['email_id','account_id','account_name']
        widgets={
            'email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'account_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'account_name': forms.TextInput(attrs={'class': 'form-control'}),
        }