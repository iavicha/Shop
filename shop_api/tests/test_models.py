from django.test import TestCase
from ..models import Cart, User, Product


class TestCart(TestCase):
    def test_str(self):
        user = User.objects.create(email='1@mail.ru', first_name= 'John', last_name='Smith')
        product = Product.objects.create(name='an apple', price='10', discount_price='80', discount='20',
                                         type='vegetables')
        Cart.objects.create(user=user, product=product, count=1)
        cart= Cart.objects.get(pk=1)
        self.assertEqual(str(cart), '1 - User... - Product ...')
        self.assertEqual(Cart.Meta.unique_together, ('user', 'product'))
