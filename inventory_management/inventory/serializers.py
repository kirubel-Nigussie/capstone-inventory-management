from rest_framework import serializers
from .models import Inventory, InventoryChangeLog

class InventorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    date_added = serializers.ReadOnlyField()
    last_updated = serializers.ReadOnlyField()

    class Meta:
        model = Inventory
        fields = '__all__'

class InventoryChangeLogSerializer(serializers.ModelSerializer):
    item_name = serializers.ReadOnlyField(source='item.name')
    changed_by = serializers.ReadOnlyField(source='changed_by.username')

    class Meta:
        model = InventoryChangeLog
        fields = ['id', 'item', 'item_name', 'changed_by', 'change_type', 'quantity_change', 'timestamp']
