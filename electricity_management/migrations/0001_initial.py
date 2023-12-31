# Generated by Django 4.2.7 on 2023-11-29 23:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_type', models.CharField(choices=[('household', 'Household'), ('industrial', 'Industrial'), ('business', 'Business')], max_length=20)),
                ('appliances', models.CharField(choices=[('refrigerator', 'Refrigerator'), ('washing_machine', 'Washing Machine'), ('air_conditioner', 'Air Conditioner'), ('microwave_oven', 'Microwave Oven'), ('television', 'Television'), ('computer', 'Computer'), ('dishwasher', 'Dishwasher'), ('coffee_maker', 'Coffee Maker'), ('toaster', 'Toaster'), ('blender', 'Blender')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PowerControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appliance_name', models.CharField(choices=[('refrigerator', 'Refrigerator'), ('washing_machine', 'Washing Machine'), ('air_conditioner', 'Air Conditioner'), ('microwave_oven', 'Microwave Oven'), ('television', 'Television'), ('computer', 'Computer'), ('dishwasher', 'Dishwasher'), ('coffee_maker', 'Coffee Maker'), ('toaster', 'Toaster'), ('blender', 'Blender')], max_length=50)),
                ('is_active', models.BooleanField(default=False)),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electricity_management.consumer')),
            ],
        ),
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumed_units', models.FloatField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('demand_request', models.BooleanField(default=False)),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electricity_management.consumer')),
            ],
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_date', models.DateField()),
                ('total_units', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electricity_management.consumer')),
            ],
        ),
    ]
