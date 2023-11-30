from django.urls import path
from . import views

app_name = 'electricity_management'

urlpatterns = [
    path('add_consumer/', views.add_consumer, name='add_consumer'),
    path('view_consumption/', views.view_consumption, name='view_consumption'),
    path('request_demand/', views.request_demand, name='request_demand'),
    path('view_billing/', views.view_billing, name='view_billing'),
    path('control_appliances/', views.control_appliances, name='control_appliances'),
]
