from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['PATCH'])
def update_product_quantity(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.quantity -= request.data.get('quantity', 1)
    product.save()
    return Response({'message': 'Quantity updated'})

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Product created'})
    return Response(serializer.errors, status=400)    

@api_view(['DELETE'])
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return Response({'message': 'Product deleted'})

