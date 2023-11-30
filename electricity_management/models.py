# electricity_management/models.py
from django.db import models
from django.contrib.auth.models import User

# Global choices for the appliance_name field
APPLIANCE_CHOICES = [
    ('refrigerator', 'Refrigerator'),
    ('washing_machine', 'Washing Machine'),
    ('air_conditioner', 'Air Conditioner'),
    ('microwave_oven', 'Microwave Oven'),
    ('television', 'Television'),
    ('computer', 'Computer'),
    ('dishwasher', 'Dishwasher'),
    ('coffee_maker', 'Coffee Maker'),
    ('toaster', 'Toaster'),
    ('blender', 'Blender'),
]

class Consumer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consumer_type = models.CharField(max_length=20, choices=[('household', 'Household'), ('industrial', 'Industrial'), ('business', 'Business')])
    appliances = models.CharField(max_length=50, choices=APPLIANCE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.consumer_type}"

class Consumption(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    consumed_units = models.FloatField(default=0)  # Default to 0
    timestamp = models.DateTimeField(auto_now_add=True)
    demand_request = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.consumer.user.username} - {self.timestamp}"

class Billing(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    billing_date = models.DateField()
    total_units = models.FloatField()
    total_amount = models.FloatField()

    def __str__(self):
        return f"{self.consumer.user.username} - {self.billing_date}"

class PowerControl(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    appliance_name = models.CharField(max_length=50, choices=APPLIANCE_CHOICES)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.consumer.user.username} - {self.appliance_name}"
