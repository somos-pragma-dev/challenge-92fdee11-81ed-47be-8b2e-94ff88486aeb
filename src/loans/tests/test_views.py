from django.urls import reverse
from rest_framework.test import APITestCase
from..models import Loan

class LoanViewSetTest(APITestCase):
    def test_create_loan(self):
        url = reverse('loan-list')
        data = {
            'amount': 1000,
            'term': 12,
            'interest_rate': 5.0,
            'status': 'pending'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)