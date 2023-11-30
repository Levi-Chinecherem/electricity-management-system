# accounts/urls.py
from django.urls import path
from .views import login_view, logout_view, signup_view, change_password_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('change-password/', change_password_view, name='change_password'),
]
