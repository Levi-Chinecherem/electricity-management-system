# electricity_management/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from .forms import AddConsumerForm, DemandRequestForm
from .models import APPLIANCE_CHOICES, Consumer, Consumption, Billing, PowerControl
from django.db.models import Sum
from datetime import timedelta

@login_required
@transaction.atomic
def add_consumer(request):
    appliance_choices = APPLIANCE_CHOICES

    if request.method == 'POST':
        form = AddConsumerForm(request.POST)
        if form.is_valid():
            consumer = form.save(commit=False)
            consumer.user = request.user
            consumer.save()

            # Create Consumption
            consumed_units = 10.0 if consumer.consumer_type == 'household' else 20.0 if consumer.consumer_type == 'industrial' else 15.0
            consumption = Consumption.objects.create(consumer=consumer, consumed_units=consumed_units)

            # Create Billing
            billing_date = consumer.user.date_joined.date() + timedelta(days=30)
            consumed_units = consumer.consumption_set.filter(timestamp__lte=billing_date).aggregate(Sum('consumed_units'))['consumed_units__sum'] or 0
            days_in_month = (billing_date - (billing_date - timedelta(days=1)).replace(day=1)).days
            total_units = consumed_units * (billing_date.day / days_in_month)
            total_amount = total_units * 200.0
            billing = Billing.objects.create(consumer=consumer, billing_date=billing_date, total_units=total_units, total_amount=total_amount)

            # Create PowerControl
            power_control = PowerControl.objects.create(consumer=consumer, appliance_name=consumer.appliances, is_active=True)

            messages.success(request, 'Consumer added successfully.')
            return redirect('electricity_management:view_consumption')
    else:
        form = AddConsumerForm()

    return render(request, 'electricity_management/add_consumer.html', {'form': form, 'appliance_choices': appliance_choices})


@login_required
def view_consumption(request):
    user = request.user
    try:
        consumers = user.consumer_set.all()  # Reverse relation for ForeignKey
        consumptions = Consumption.objects.filter(consumer__in=consumers).order_by('-timestamp')
    except Consumer.DoesNotExist:
        consumers = None
        consumptions = []

    return render(request, 'electricity_management/view_consumption.html', {'consumers': consumers, 'consumptions': consumptions})

@login_required
def request_demand(request):
    if request.method == 'POST':
        consumer = request.user.consumer_set.first()  # Get the first related consumer
        demand_request = request.POST.get('demand_request', False)

        # Ensure demand_request is a boolean
        demand_request = demand_request.lower() == 'true'

        # Try to get the latest consumption record
        latest_consumption = consumer.consumption_set.order_by('-timestamp').first()

        if latest_consumption:
            # Update the existing record
            latest_consumption.demand_request = demand_request
            latest_consumption.save()
        else:
            # Create a new record if none exists
            Consumption.objects.create(consumer=consumer, demand_request=demand_request)

        messages.success(request, 'Demand request updated successfully.')
        return redirect('electricity_management:view_consumption')

    return render(request, 'electricity_management/request_demand.html')

@login_required
def view_billing(request):
    user = request.user
    try:
        consumers = user.consumer_set.all()  # Reverse relation for ForeignKey
        billings = Billing.objects.filter(consumer__in=consumers).order_by('-billing_date')
    except Consumer.DoesNotExist:
        consumers = None
        billings = []

    return render(request, 'electricity_management/view_billing.html', {'consumers': consumers, 'billings': billings})

@login_required
def control_appliances(request):
    consumers = request.user.consumer_set.all()  # Reverse relation for ForeignKey
    appliances = PowerControl.objects.filter(consumer__in=consumers)
    return render(request, 'electricity_management/control_appliances.html', {'appliances': appliances})


