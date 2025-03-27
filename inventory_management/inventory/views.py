from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes





@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def inventory_list(request):
    if request.method == 'GET':
        items = Inventory.objects.all()
        serializer = InventorySerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

