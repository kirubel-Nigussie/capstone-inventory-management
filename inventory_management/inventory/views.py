from rest_framework import generics, permissions, filters
from .models import Inventory, InventoryChangeLog
from .serializers import InventorySerializer, InventoryChangeLogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

class InventoryListCreateView(generics.ListCreateAPIView):
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Inventory.objects.filter(owner=self.request.user)

       
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

       
        low_stock = self.request.query_params.get('low_stock')
        if low_stock:
            queryset = queryset.filter(quantity__lt=5)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class InventoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Inventory.objects.filter(owner=self.request.user)

class InventoryChangeLogView(generics.ListAPIView):
    serializer_class = InventoryChangeLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InventoryChangeLog.objects.filter(item__owner=self.request.user)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def restock_inventory(request, pk):
    item = Inventory.objects.get(id=pk, owner=request.user)
    quantity = int(request.data.get('quantity', 0))

    if quantity > 0:
        item.quantity += quantity
        item.save()
        InventoryChangeLog.objects.create(item=item, changed_by=request.user, change_type='restock', quantity_change=quantity)
        return Response({'message': f'Restocked {quantity} units. New quantity: {item.quantity}'})
    return Response({'error': 'Invalid quantity'}, status=400)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def sell_inventory(request, pk):
    item = Inventory.objects.get(id=pk, owner=request.user)
    quantity = int(request.data.get('quantity', 0))

    if quantity > 0 and item.quantity >= quantity:
        item.quantity -= quantity
        item.save()
        InventoryChangeLog.objects.create(item=item, changed_by=request.user, change_type='sold', quantity_change=-quantity)
        return Response({'message': f'Sold {quantity} units. New quantity: {item.quantity}'})
    return Response({'error': 'Not enough stock or invalid quantity'}, status=400)

