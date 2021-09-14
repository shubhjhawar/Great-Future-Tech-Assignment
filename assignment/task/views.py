from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class DataView(viewsets.ModelViewSet):
    serializer_class = DataSerializer

    @action(detail=False, methods=['POST'], url_path='add')
    def add_data(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":"data registered successfully"}, status=status.HTTP_201_CREATED)
        return Response({"failure":"something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'], url_path='show')
    def show_data(self, request):
        # queryset = DataModel.objects.get(id=1)
        queryset = DataModel.objects.all()
        product_list=[]
        for object in queryset:
            product_details ={}
            product_details['ProductName'] = object.ProductName
            product_details['ProductID'] = object.ProductID
            product_details['ProductQuantity'] = object.ProductQuantity
            product_list.append(product_details)
        return Response(product_list, status=status.HTTP_200_OK)