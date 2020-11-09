from django.urls import path
from .views import IndexView, ShopViews

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('shop/', ShopViews.as_view(), name='shop')
]
