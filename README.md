Overview of Inventory Management System
Purpose: This code implements an inventory management system for handling food items, including functionalities for adding, editing, deleting, and searching items, as well as generating reports based on expiry dates and stock levels.

Initialization (__init__ method):

Initializes the Inventory object with an optional CSV filename for data storage.
Loads existing inventory data from the CSV file using FileManager.
Adding, Editing, and Deleting Items:

add_item(item): Adds a new item to the inventory and updates the CSV file.
edit_item(barcode, new_item): Modifies an existing item's details based on its barcode and writes changes to the CSV.
delete_item(barcode): Removes an item from the inventory by its barcode and updates the CSV.
Searching for Items:

search_item(name): Searches for items by name (case insensitive).
search_item_by_barcode(barcode): Retrieves an item by its barcode.
search_item_by_category(category): Finds items by category (case insensitive).
search_items(keyword): Searches for items by barcode, name, or category.
Generating Reports:

near_expiry_items(threshold_days): Returns items nearing expiry within a specified threshold.
items_in_low_stock(threshold_quantity): Identifies items with stock below a specified threshold.
category_summaries(): Summarizes inventory items by category.
generate_expiry_report(threshold_days): Generates a report of items nearing expiry with days until expiry.
Iterator and Generator:

Implements __iter__ and __next__ methods to iterate through inventory items.
generate_near_expiry_items(threshold_days): A generator yielding items nearing their expiry date.
File Management:

Utilizes FileManager for reading from and writing to a CSV file (read_from_csv and write_to_csv methods).
This inventory management system provides robust functionalities for managing food items, handling CRUD operations, generating reports based on expiry and stock levels, and facilitating efficient data storage and retrieval through CSV files.
