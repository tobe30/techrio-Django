from django.contrib import admin
from core.models import PaymentRequest, ContactMessage
# Register your models here.


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'submitted_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    readonly_fields = ('submitted_at',)
    
admin.site.register(PaymentRequest)
admin.site.register(ContactMessage, ContactMessageAdmin)
