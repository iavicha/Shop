from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .settings.base import INFO


# Create your views here.

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        context = INFO # Должен быть словарём
        return render(request, 'myshop/index.html', context)


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
