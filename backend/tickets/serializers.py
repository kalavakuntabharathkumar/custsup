from rest_framework import serializers
from .models import Ticket
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields=['id','subject','description','requester_email','assigned_to','status','priority','created_at','updated_at']
        read_only_fields=['id','created_at','updated_at']
