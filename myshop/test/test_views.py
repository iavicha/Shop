from django.test import TestCase
from django.shortcuts import reverse
from django.test.utils import override_settings
from rest_framework import status


class TestShopView(TestCase):
    @override_settings(DEBUG=False)
    def test_get(self):
        response = self.client.get('/shop/')
        self.assertAlmostEqual(response.status_code, status.HTTP_200_OK)

    @override_settings(DEBUG=False)
    def test_reverse(self):
        response = self.client.get(reverse('shop'))
        self.assertAlmostEqual(response.status_code, 200)

    @override_settings(DEBUG=False)
    def test_template(self):
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myshop/shop.html')


class TestHomeView(TestCase):
    @override_settings(DEBUG=False)
    def test_get_home(self):
        response = self.client.get('/')
        self.assertAlmostEqual(response.status_code, status.HTTP_200_OK)

    @override_settings(DEBUG=False)
    def test_reverse_home(self):
        response = self.client.get('/')
        self.assertAlmostEqual(response.status_code, 200)

    @override_settings(DEBUG=False)
    def test_template_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myshop/login.html')