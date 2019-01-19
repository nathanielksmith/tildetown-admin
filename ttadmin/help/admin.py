from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('submitted', 'issue_status', 'issue_type', 'name', 'email')
    list_filter = ('issue_status', 'issue_type')
    fields = ('name', 'email', 'issue_status', 'issue_type', 'issue_text')
