from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .models import User, Product, Coupon, Cart
from .serializers import UserSerializer, ProductSerializer, CouponSerializer, CartSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        filter_param = {param: request.GET[param] for param in request.GET}

        queryset = self.get_queryset()
        filter_queryset = queryset.filter(**filter_param)

        serializer = self.get_serializer(filter_queryset, many=True)

        return Response(serializer.data)


class CouponViesSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CartViewsSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """
           API корзины

           list:
           Выводим список содержимого корзины

           create:
           Создаем корзину.

           delete:
           Удалить содержимое корзины


           add:
           Добавить в корзину продукта
           """

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset.filter(user=kwargs['pk']), many=True)

        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def add(self, request, pk=None):
        print(request.user)
        product = Product.objects.get(pk=pk)
        user = request.GET['user']
        count = request.GET['count']

        queryset = self.get_queryset()
        data = dict(user=user.pk, product=product.pk, count=count)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        queryset.create(**serializer.data)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
