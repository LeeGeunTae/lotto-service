from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buy/', views.buy_ticket, name='buy_ticket'),
    path('check/', views.check_ticket, name='check_ticket'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
]
