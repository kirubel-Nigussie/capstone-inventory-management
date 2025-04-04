from django.urls import path
from .views import (
    InventoryListCreateView, InventoryRetrieveUpdateDeleteView,
    restock_inventory, sell_inventory, InventoryChangeLogView
)

urlpatterns = [
    path('inventory/', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('inventory/<int:pk>/', InventoryRetrieveUpdateDeleteView.as_view(), name='inventory-detail'),
    path('inventory/<int:pk>/restock/', restock_inventory, name='restock-inventory'),
    path('inventory/<int:pk>/sell/', sell_inventory, name='sell-inventory'),
    path('inventory/logs/', InventoryChangeLogView.as_view(), name='inventory-change-logs'),
]
