from django.urls import path
from .views import IndexView, ShopViews, AboutView, BlogView, CartView
from .views import ContactView, ProductSingleView, WishListView,ChekoutView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('shop/', ShopViews.as_view(), name='shop'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('cart/', CartView.as_view(), name='cart'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('product/', ProductSingleView.as_view(), name='product'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('checkout/', ChekoutView.as_view(), name='checkout')
]
