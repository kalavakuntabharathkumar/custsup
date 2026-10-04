from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny
from .models import Ticket
from .serializers import TicketSerializer
class TicketViewSet(viewsets.ModelViewSet):
    queryset=Ticket.objects.all()
    serializer_class=TicketSerializer
    permission_classes=[AllowAny]  # Demo only: replace with authenticated permissions before deployment.
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    search_fields=['subject','description','requester_email','assigned_to']
    ordering_fields=['created_at','updated_at','priority','status']
    def get_queryset(self):
        qs=super().get_queryset()
        status=self.request.query_params.get('status')
        priority=self.request.query_params.get('priority')
        if status: qs=qs.filter(status=status)
        if priority: qs=qs.filter(priority=priority)
        return qs
