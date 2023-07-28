from django.urls import path, include

from .views import ProductList, CategoryList, CategoryProduct
from rest_framework import routers

router = routers.SimpleRouter()
router.register('products', ProductList, basename='products')
router.register('category', CategoryList, basename='category')
router.register('categoryBasedProducts', CategoryProduct, basename='categoryBasedProducts')

urlpatterns = [
   path('', include(router.urls) ) 
]
