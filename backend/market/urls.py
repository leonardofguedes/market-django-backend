from django.urls import path, include
from rest_framework import routers
from .viewsets import ProductViewSet, update_product_quantity, create_product, delete_product

router = routers.DefaultRouter()
router.register(r'produtos', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('produtos/<int:pk>/update_quantity/', update_product_quantity, name='update_product_quantity'),
    path('produtos/create/', create_product, name='create_product'),
    path('produtos/<int:pk>/delete/', delete_product, name='delete_product'),
]