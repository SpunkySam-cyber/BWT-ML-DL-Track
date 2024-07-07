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

    def __iter__(self):
            """
            Iterator method to iterate through food items in the inventory.
            """
            self._index = 0
            return self

    def __next__(self):
            """
            Next method for iterator to retrieve the next food item.
            """
            if self._index < len(self.items):
                item = self.items[self._index]
                self._index += 1
                return item
            else:
                raise StopIteration

    def update_item(self, barcode, new_item):
            """
            Update an existing item in the inventory based on its barcode.

            Args:
            - barcode (str): Barcode of the item to be updated.
            - new_item (dict): Dictionary containing updated item details ('name', 'category', 'quantity', 'expiry_date').

            Returns:
            - bool: True if the item was successfully updated, False otherwise.
            """
            for item in self.items:
                if item['barcode'] == barcode:
                    item.update(new_item)  # Update item details
                    self.file_manager.write_to_csv(self.items)  # Write changes to CSV
                    return True
            return False

    def generate_near_expiry_items(self, threshold_days=7):
            """
            Generator to yield food items that are nearing their expiry date.

            Args:
            - threshold_days (int): Number of days within which an item is considered near expiry. Default is 7 days.

            Yields:
            - dict: Each food item that is nearing its expiry date.
            """
            today = date.today()
            for item in self.items:
                expiry_date = item.get('expiry_date')
                if expiry_date:
                    if (expiry_date - today).days <= threshold_days:
                        yield item

    def items_in_low_stock(self, threshold_quantity=5):
        """
        Retrieve items in the inventory that are in low stock.

        Args:
        - threshold_quantity (int): Threshold quantity below which items are considered low stock. Default is 5.

        Returns:
        - list: List of items that are in low stock.
        """
        low_stock_items = []
        for item in self.items:
            if item['quantity'] < threshold_quantity:
                low_stock_items.append(item)
        return low_stock_items

    def category_summaries(self):
        """
        Generate summaries of inventory items by category.

        Returns:
        - dict: Dictionary where keys are categories and values are lists of items in each category.
        """
        category_dict = {}
        for item in self.items:
            category = item['category']
            if category not in category_dict:
                category_dict[category] = []
            category_dict[category].append(item)
        return category_dict

    def generate_expiry_report(self, threshold_days=30):
        """
        Generate a report of items nearing their expiry date.

        Args:
        - threshold_days (int): Number of days within which an item is considered nearing expiry. Default is 30 days.

        Returns:
        - list: List of tuples (item, days_until_expiry) for items nearing expiry.
        """
        today = date.today()
        expiry_report = []
        for item in self.items:
            expiry_date = item.get('expiry_date')
            if expiry_date:
                days_until_expiry = (expiry_date - today).days
                if days_until_expiry <= threshold_days:
                    expiry_report.append((item, days_until_expiry))
        return expiry_report

    def search_item_by_barcode(self, barcode):
        """
        Search for an item in the inventory by its barcode.

        Args:
        - barcode (str): Barcode of the item to search for.

        Returns:
        - dict or None: Item dictionary if found, None if not found.
        """
        for item in self.items:
            if item['barcode'] == barcode:
                return item
        return None

    def search_item_by_name(self, name):
        """
        Search for items in the inventory by their name (case insensitive).

        Args:
        - name (str): Name (or part of the name) of the item to search for.

        Returns:
        - list: List of items matching the search criteria.
        """
        results = []
        for item in self.items:
            if name.lower() in item['name'].lower():
                results.append(item)
        return results

    def search_item_by_category(self, category):
        """
        Search for items in the inventory by their category (case insensitive).

        Args:
        - category (str): Category (or part of the category) of the items to search for.

        Returns:
        - list: List of items matching the search criteria.
        """
        results = []
        for item in self.items:
            if category.lower() in item['category'].lower():
                results.append(item)
        return results

    def search_items(self, keyword):
        """
        Search for items in the inventory by barcode, name, or category.

        Args:
        - keyword (str): Keyword to search for (barcode, name, or category).

        Returns:
        - list: List of items matching the search criteria.
        """
        results = []
        # Check if keyword matches barcode
        item = self.search_item_by_barcode(keyword)
        if item:
            results.append(item)
        # Check if keyword matches name
        results.extend(self.search_item_by_name(keyword))
        # Check if keyword matches category
        results.extend(self.search_item_by_category(keyword))

        return results
