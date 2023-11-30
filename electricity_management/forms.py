# electricity_management/forms.py
from django import forms
from .models import APPLIANCE_CHOICES, Consumer

class AddConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ['consumer_type', 'appliances']
        widgets = {
            'consumer_type': forms.Select(attrs={'class': 'form-control'}),
            'appliances': forms.Select(attrs={'class': 'form-control'}),
        }

class DemandRequestForm(forms.Form):
    demand_request = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
