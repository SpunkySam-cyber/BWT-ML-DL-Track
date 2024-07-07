from inventory_management.inventory.Inventory import Inventory
from datetime import date, timedelta

# Create an instance of Inventory
inventory = Inventory()
"""print("Current items in inventory:")
for item in inventory.items:
    print(item)"""

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

]


# Add each item to the inventory
for item in items_to_add:
    inventory.add_item(item)

"""Now running the sample script that uses all the methods that
 are previously defined and also all the functionalities.
 These include 
 1.displaying the whole inventory
 2.Generating items using generators method in inventory file that are nearing expiry
 3.Generating an expiry report which show how many days each item has left until it expires.
 4.Searching for items and generating items in low stock
 """

# Example: Iterating through all items
print("Iterating through all items:")
for item in inventory:
    print(item)

# Example: Generating items nearing expiry using generator
print("\nGenerating items nearing expiry:")
for item in inventory.generate_near_expiry_items(threshold_days=10):
    print(item)

# Example: Searching for items
print("\nSearching for items by keyword 'Soft Drinks':")
results = inventory.search_items('Soft Drinks')
for item in results:
    print(item)

# Example: Generating items in low stock
print("\nGenerating items in low stock:")
low_stock_items = inventory.items_in_low_stock(threshold_quantity=5)
for item in low_stock_items:
    print(item)

# Example: Generating category summaries
print("\nGenerating category summaries:")
category_summaries = inventory.category_summaries()
for category, items in category_summaries.items():
    print(f"Category: {category}")
    for item in items:
        print(f"  {item}")

# Example: Generating expiry report
print("\nGenerating expiry report:")
expiry_report = inventory.generate_expiry_report(threshold_days=30)
for item, days_until_expiry in expiry_report:
    print(f"{item} - Days until expiry: {days_until_expiry}")
