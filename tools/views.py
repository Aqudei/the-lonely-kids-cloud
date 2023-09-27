from django.shortcuts import render
from rest_framework import generics
from tools.models import Variant
from tools.serializers import (
    VariantSerializer
)
from rest_framework import filters, pagination

# Create your views here.
class VariantListAPIView(generics.ListAPIView):
    """
    docstring
    """
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['sku', 'product__handle','title']
    pagination_class = pagination.LimitOffsetPagination
