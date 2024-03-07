from rest_framework .viewsets import ModelViewSet
from .serializers import ProductSerializer
from .models import Product
from rest_framework import permissions


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]