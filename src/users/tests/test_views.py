from django.urls import reverse
from rest_framework.test import APITestCase
from..models import User

class UserViewSetTest(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)