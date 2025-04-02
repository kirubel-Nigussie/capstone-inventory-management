from django.db import models
from django.contrib.auth.models import User

class Inventory(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('food', 'Food'),
        ('furniture', 'Furniture'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.quantity} left"
    



class InventoryChangeLog(models.Model):
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="change_logs")
    changed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    change_type = models.CharField(max_length=20, choices=[('restock', 'Restock'), ('sold', 'Sold')])
    quantity_change = models.IntegerField()

    def __str__(self):
        return f"{self.item.name} - {self.change_type} - {self.quantity_change}"

