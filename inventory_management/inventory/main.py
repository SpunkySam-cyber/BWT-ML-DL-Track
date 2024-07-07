
from inventory_management.inventory.Inventory import Inventory
from datetime import date, timedelta

# Create an instance of Inventory
inventory = Inventory()
print("Current items in inventory:")
for item in inventory.items:
    print(item)

# Clear all items in the inventory
inventory.items = []
# Write the empty list of items to the CSV file
inventory.file_manager.write_to_csv(inventory.items)

# List of 10 items to add
items_to_add = [
    {'name': 'Apples', 'category': 'Fruits', 'quantity': 5, 'barcode': '10001', 'expiry_date': date.today() + timedelta(days=14)},
    {'name': 'Oranges', 'category': 'Fruits', 'quantity': 3, 'barcode': '10002', 'expiry_date': date.today() + timedelta(days=10)},
    {'name': 'Oreo Biscuit', 'category': 'Snacks', 'quantity': 2, 'barcode': '10003', 'expiry_date': date.today() + timedelta(days=120)},
    {'name': 'Soft Drinks', 'category': 'Beverages', 'quantity': 10, 'barcode': '10004', 'expiry_date': date.today() + timedelta(days=30)},
    {'name': 'Lays', 'category': 'Snacks', 'quantity': 4, 'barcode': '10005', 'expiry_date': date.today() + timedelta(days=235)},
    {'name': 'Coffee Beans', 'category': 'Beverages', 'quantity': 1, 'barcode': '10006', 'expiry_date': date.today() + timedelta(days=365)},
    {'name': 'Milk', 'category': 'Dairy', 'quantity': 2, 'barcode': '10007', 'expiry_date': date.today() + timedelta(days=7)},
    {'name': 'Cookies', 'category': 'Snacks', 'quantity': 3, 'barcode': '10008', 'expiry_date': date.today() + timedelta(days=90)},
    {'name': 'Yoghurt', 'category': 'Dairy', 'quantity': 4, 'barcode': '10009', 'expiry_date': date.today() + timedelta(days=5)},
    {'name': 'Water', 'category': 'Beverages', 'quantity': 15, 'barcode': '10010', 'expiry_date': None}
]

# Add each item to the inventory
for item in items_to_add:
    inventory.add_item(item)
