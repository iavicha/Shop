from django.test import TestCase
from django.shortcuts import reverse
from django.test.utils import override_settings
from rest_framework import status


class TestAPIView(TestCase):
    @override_settings(DEBUG=False)
    def test_get(self):
        response = self.client.get('/api/')
        self.assertAlmostEqual(response.status_code, status.HTTP_200_OK)
