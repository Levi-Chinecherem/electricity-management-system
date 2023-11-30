from django.contrib import admin
from .models import Consumer, Consumption, Billing, PowerControl

# Customize the Django admin site
admin.site.site_header = 'Electricity Management System Admin'
admin.site.site_title = 'EMS Admin'
admin.site.index_title = 'Welcome to the Electricity Management System Admin'
admin.site.site_url = '/electricity_management/'  # Set the URL to the desired path

class ConsumerAdmin(admin.ModelAdmin):
    list_display = ('user', 'consumer_type', 'appliances')

class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ('consumer', 'consumed_units', 'timestamp', 'demand_request')

class BillingAdmin(admin.ModelAdmin):
    list_display = ('consumer', 'billing_date', 'total_units', 'total_amount')

class PowerControlAdmin(admin.ModelAdmin):
    list_display = ('consumer', 'appliance_name', 'is_active')

admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(Consumption, ConsumptionAdmin)
admin.site.register(Billing, BillingAdmin)
admin.site.register(PowerControl, PowerControlAdmin)
