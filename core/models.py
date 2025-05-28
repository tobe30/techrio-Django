from django.db import models

class PaymentRequest(models.Model):
    PLAN_CHOICES = [
        ('Individual', 'Individual'),
        ('Company', 'Company'),
        ('Enterprise', 'Enterprise'),
    ]

    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    amount = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    paid = models.BooleanField(default=False)
    payment_reference = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.plan} - ₦{self.amount}"


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"