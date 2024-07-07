from .file_manager import FileManager
from .food_item import FoodItem
from datetime import date, timedelta


class Inventory:
    def __init__(self, filename="inventory.csv"):
        """
        Initialize Inventory object.

        Args:
        - filename (str): Optional, CSV filename to read/write inventory data.
        """
        self.items = []
        self.filename = filename
        self.file_manager = FileManager(self.filename)
        self.read_from_csv()  # Load inventory data from CSV on initialization

    def add_item(self, item):
        """
        Add a new item to the inventory and immediately write to CSV.

        Args:
        - item (dict): Dictionary containing item details ('name', 'category', 'quantity', 'barcode', 'expiry_date').
        """
        self.items.append(item)
        self.file_manager.write_to_csv(self.items)

    def edit_item(self, barcode, new_item):
        """
        Edit an existing item in the inventory based on its barcode.

        Args:
        - barcode (str): Barcode of the item to be edited.
        - new_item (dict): Dictionary containing updated item details ('name', 'category', 'quantity', 'expiry_date').

        Returns:
        - bool: True if the item was successfully edited, False otherwise.
        """
        for item in self.items:
            if item['barcode'] == barcode:
                item.update(new_item)  # Update item details
                self.file_manager.write_to_csv(self.items)  # Write changes to CSV
                return True
        return False

    def delete_item(self, barcode):
        """
        Delete an item from the inventory based on its barcode.

        Args:
        - barcode (str): Barcode of the item to be deleted.

        Returns:
        - bool: True if the item was successfully deleted, False otherwise.
        """
        for i, item in enumerate(self.items):
            if item['barcode'] == barcode:
                del self.items[i]  # Delete item from list
                self.file_manager.write_to_csv(self.items)  # Write updated inventory to CSV
                return True
        return False

    def search_item(self, name):
        """
        Search for items in the inventory based on their name.

        Args:
        - name (str): Name (or part of the name) of the item to search for.

        Returns:
        - list: List of items matching the search criteria.
        """
        results = []
        for item in self.items:
            if name.lower() in item['name'].lower():  # Case insensitive search
                results.append(item)
        return results

    def near_expiry_items(self, threshold_days=7):
        """
        Retrieve items from the inventory that are near their expiry date.

        Args:
        - threshold_days (int): Number of days within which an item is considered near expiry. Default is 7 days.

        Returns:
        - list: List of items that are near expiry.
        """
        today = date.today()
        expiry_list = []
        for item in self.items:
            expiry_date = item.get('expiry_date')
            if expiry_date:
                if (expiry_date - today).days <= threshold_days:
                    expiry_list.append(item)
        return expiry_list

    def read_from_csv(self):
        """
        Read inventory data from CSV file and populate self.items list.
        """
        self.items = self.file_manager.read_from_csv()

