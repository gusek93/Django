from django import forms
from django.db.models import fields
from django.db.models.fields import PositiveBigIntegerField
from .models import PaymentDivision


class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentDivision
        fields = '__all__'