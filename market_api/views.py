from django.shortcuts import render
from .models import Product, Category
from .serializers import  ProductSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'name'
    
    
class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'name'
        
class CategoryProduct(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Product.objects.filter(category=pk)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)