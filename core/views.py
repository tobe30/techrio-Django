import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import PaymentRequest
import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ContactMessageForm

FLW_SECRET_KEY = 'FLWSECK_TEST-34d7cb78972b12d38736e20f579c0068-X'
FLW_BASE_URL = 'https://api.flutterwave.com/v3/payments'


def index(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been submitted successfully!')
            return redirect('core:index')  # Replace 'contact' with your actual URL name
    else:
        form = ContactMessageForm()
    return render(request, 'core/index.html', {'form': form})

@csrf_exempt
def start_payment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            plan = data.get('plan')
            amount = int(data.get('amount'))  # ensure int
            name = data.get('name')
            email = data.get('email')

            # Save payment request
            payment = PaymentRequest.objects.create(
                plan=plan,
                amount=amount,
                customer_name=name,
                customer_email=email,
            )
# https://fbf4-105-112-106-180.ngrok-free.app
            payload = {
                "tx_ref": f"techrio-{payment.id}",
                "amount": str(amount),
                "currency": "NGN",
                "redirect_url": f"https://techrio-django.onrender.com/payment-callback/{payment.id}/",
                "customer": {
                    "email": email,
                    "name": name,
                },
                "customizations": {
                    "title": "Techrio Payment",
                    "description": f"Payment for {plan} plan",
                }
            }

            headers = {
                "Authorization": f"Bearer {FLW_SECRET_KEY}",
                "Content-Type": "application/json"
            }

            response = requests.post(FLW_BASE_URL, json=payload, headers=headers)
            try:
                result = response.json()
            except json.JSONDecodeError:
                return JsonResponse({'status': 'error', 'message': 'Invalid response from payment gateway.'})

            if response.status_code == 200 and result.get('status') == 'success':
                payment_link = result['data']['link']
                return JsonResponse({'status': 'success', 'payment_link': payment_link})
            else:
                # Log full error for debugging
                error_msg = result.get('message') or 'Could not initialize payment.'
                return JsonResponse({'status': 'error', 'message': error_msg})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error: {str(e)}'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def payment_callback(request, payment_id):
    transaction_id = request.GET.get('transaction_id')

    if not transaction_id:
        return render(request, 'core/payment_failed.html', {"error": "No transaction ID provided."})

    # Call Flutterwave to verify the transaction
    verify_url = f"https://api.flutterwave.com/v3/transactions/{transaction_id}/verify"
    headers = {
        "Authorization": f"Bearer {FLW_SECRET_KEY}"
    }

    response = requests.get(verify_url, headers=headers)
    result = response.json()

    if result['status'] == 'success' and result['data']['status'] == 'successful':
        payment = get_object_or_404(PaymentRequest, id=payment_id)

        # Only mark as paid if it hasn't been already
        if not payment.paid:
            payment.paid = True
            payment.payment_reference = transaction_id
            payment.save()

        return render(request, 'core/payment_success.html', {'payment': payment})
    else:
        return render(request, 'core/payment_failed.html', {
            "error": result.get("message", "Payment verification failed.")
        })
        
def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been submitted successfully!')
            return redirect('contact')  # Replace 'contact' with your actual URL name
    else:
        form = ContactMessageForm()
    
    return render(request, 'core/index.html', {'form': form})
