from django.shortcuts import render,get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serilalizers
from .models import Order
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User= get_user_model()

class OrderCreateListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serilalizers.OrderCreationSerializer
    queryset = Order.objects.all()
    def get(self,request):
        orders= Order.objects.all()
        serializer = self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        data = request.data
        user= request.user

        serializer= self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(generics.GenericAPIView):
    serializer_class = serilalizers.OrderDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request,order_id):
        order = get_object_or_404(Order, id=order_id)

        serializer = self.serializer_class(instance=order)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,order_id):
        user = request.user

        order = get_object_or_404(Order,pk=order_id)

        serilalizer = self.serializer_class(data=data, instance=order)

        if serilalizer.is_valid():
            serilalizer.save()
            return Response(data=serilalizer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,order_id):
        order = get_object_or_404(Order,pk=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class updateOrderStatus(generics.GenericAPIView):
    serializer_class = serilalizers.OrderStatusUpdate
    permission_classes = [IsAuthenticated]

    def put(self,request,order_id):
        order = get_object_or_404(Order, order_id)

        data = request.data 

        serilalizer = self.serializer_class(data=data, instance=order)

        if serilalizer.is_valid():
            serilalizer.save()

            return Response(data=serilalizer.data, status=status.HTTP_200_OK)

        Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserOrdersListView(generics.GenericAPIView):
    serializer_class = serilalizers.OrderDetailSerializer

    def get(self,request,user_id):
        user = User.objects.get(pk=user_id) 
        
        orders = Order.objects.all().filter(customer=user)
        serilalizer = self.serializer_class(instance=orders, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)


class UserOrderDetails(generics.GenericAPIView):
    serializer_class = serilalizers.OrderDetailSerializer

    def get(self, request, user_id, order_id):
        user = User.objects.get(pk=user_id)
        order = Order.objects.all().filter(customer=user).get(pk=order_id)
        serilalizer = self.serializer_class(instance=order)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

