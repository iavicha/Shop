from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .settings.base import INFO
from shop_api.models import Product, Cart


# Create your views here.

class IndexView(View):
    def get(self, request):
        context = INFO  # Должен быть словарём
        return render(request, 'myshop/index.html', context)


class AboutView(View):
    def get(self, request):
        context = INFO
        return render(request, 'myshop/about.html', context)


class BlogView(View):
    def get(self, request):
        context = INFO
        return render(request, 'myshop/blog.html', context)


class CartView(LoginRequiredMixin, View):
    # Гд
    def get(self, request):
        cart_query_set = Cart.objects.filter(user__auth_user__username=request.user)
        d = {'page_obj': [
            {
                'image': ...,
                'name': ...,
                'discount': ...,
                'price': ...,
                'discount_price': ...,

            }
        ]}
        context = INFO
        total_price = 0
        context['page_obj'] = cart_query_set
        context['total_price'] = total_price
        return render(request, 'myshop/cart.html', context)


class ContactView(View):
    def get(self, request):
        context = INFO
        return render(request, 'myshop/contact.html', context)


class ProductSingleView(View):
    def get(self, request):
        context = INFO
        return render(request, 'myshop/product-single.html', context)


class WishListView(View):
    def get(self, request):
        context = INFO
        return render(request, 'myshop/wishlist.html', context)


class ChekoutView(View):
    def get(self, request):
        context = INFO
        return render(request, 'myshop/checkout.html', context)


class ShopViews(View):
    def get(self, request):
        page_obj = Product.objects.all()
        print(page_obj)
        d = {'page_obj': [
            {
                'image': ...,
                'name': ...,
                'discount': ...,
                'price': ...,
                'discount_price': ...,

            }
        ]}
        context = INFO
        context['page_obj'] = page_obj
        print([product.image for product in page_obj])

        return render(request, 'myshop/shop.html', context)
