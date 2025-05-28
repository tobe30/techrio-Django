from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('start-payment/', views.start_payment, name='start_payment'),
    path('payment-callback/<int:payment_id>/', views.payment_callback, name='payment_callback'),

    # You need to uncomment or add:
    # path('payment-callback/<int:payment_id>/', views.payment_callback, name='payment_callback'),

    
]
