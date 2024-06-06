from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import *
from . serializers import *

# Create your views here.

@api_view(["GET"])
def endpoints(request):
    data = {
        'api/' : 'All Endpoints',
        'api/products/' : 'Getting and Creating Products',
        'api/categories/' : 'Getting and Creating Categories',
        'api/orderItems/' : 'Getting and Creating OrderItems',
    }
    return Response(data)



class CategoryGetAndCreate(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class ProductGetAndCreate(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer