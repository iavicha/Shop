from rest_framework import routers
from .views import UserViewSet, ProductViewSet, CouponViesSet, CartViewsSet
router = routers.SimpleRouter()

router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'coupons', CouponViesSet)
router.register(r'cart', CartViewsSet)
urlpatterns = router.urls
