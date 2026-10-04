from django.contrib import admin
from .models import Ticket
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display=('id','subject','requester_email','assigned_to','status','priority','created_at')
    list_filter=('status','priority'); search_fields=('subject','requester_email','assigned_to')
