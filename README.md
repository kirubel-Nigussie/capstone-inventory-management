# Inventory Management API
## This is a backend API built using **Django** and **Django REST Framework**.
### It allows users to:
-  register
-   log in
-   manage inventory items (add, update, delete, restock, sell).

## Tech stack
- Django
- Django REST Framework
- SQLite 
- Django built-in authentication


##  API Endpoints

This API provides endpoints for user management, inventory control, and stock updates.

## Users

- `POST /api/users/register/`: Register a new user.
- `POST /api/users/login/`: Log in a user.

## Inventory

- `GET /api/inventory/`: List all items.
- `POST /api/inventory/`: Create a new item.
- `GET /api/inventory/<id>/`: View a specific item.
- `PUT /api/inventory/<id>/`: Update item info.
- `DELETE /api/inventory/<id>/`: Delete an item.

## Stock Updates

- `POST /api/inventory/<id>/restock/`: Add stock.
- `POST /api/inventory/<id>/sell/`: Reduce stock (sold).
- `GET /api/inventory/logs/`: See inventory change logs.