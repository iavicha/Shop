from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .settings.base import INFO


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


class CartView(View):
    def get(self, request):
        context = INFO
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
        d = {'page_obj': [
            {
                'image': ...,
                'name': ...,
                'discount': ...,
                'fullprice': ...,
                'pricesale': ...,

            }
        ]}
        context = INFO
        return render(request, 'myshop/shop.html', context)
