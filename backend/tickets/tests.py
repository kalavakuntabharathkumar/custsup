from django.test import TestCase
from rest_framework.test import APIClient
from .models import Ticket
class TicketApiTests(TestCase):
    def setUp(self): self.client=APIClient()
    def test_create_and_filter_ticket(self):
        response=self.client.post('/api/tickets/',{'subject':'Login issue','description':'Cannot sign in','requester_email':'demo@example.com','priority':'high'},format='json')
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data['status'],'open')
        self.assertEqual(self.client.get('/api/tickets/?priority=high').data['count'],1)
    def test_status_update(self):
        t=Ticket.objects.create(subject='Billing question',requester_email='billing@example.com')
        response=self.client.patch(f'/api/tickets/{t.id}/',{'status':'resolved'},format='json')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['status'],'resolved')
