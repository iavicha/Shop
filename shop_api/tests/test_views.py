from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.test import APITestCase
from django.test.utils import override_settings
from ..models import Product


class TestProduct(APITestCase):

    def setUp(self) -> None:
        Product.objects.create(
            name='an orange',
            price='100',
            discount_price='80',
            discount='20',
            type='fruits')

    @override_settings(DEBUG=False)
    def test_list(self):
        Product.objects.create(
            name='a tomato',
            price='100',
            discount_price='80',
            discount='20',
            type='vegetables')
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve(self):
        ...

    def test_delete(self):
        response = self.client.delete('/products/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete('/products/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Product.objects.create(
        #     name='an orange',
        #     price='100',
        #     discount_price='80',
        #     discount='20',
        #     type='fruits')

        with self.assertRaises(ObjectDoesNotExist, msg='Не найдено'):
            Product.objects.get(pk=2)


class TestCoupon(APITestCase):
    def test_not_allowed(self):
        not_allowed_methods = {
            'POST': self.client.post,
            'PUT': self.client.put,
            'PATCH': self.client.patch,
            'DELETE': self.client.delete
        }
        response = self.client.get('/coupons/')
        url = '/coupons/'
        for method_name, method in not_allowed_methods.items():
            self.assertNotEqual(
                response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED,
                msg=f'Method {method_name} should be not allowed for url: {url}')