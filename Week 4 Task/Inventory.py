import csv

class Inventory:
    def __init__(self):
        self.items = []

    def add_items(self, food_item):
        self.items.append(food_item)

    def edit_item(self, barcode, new_attributes):
        for item in self.items:
            if item.barcode == barcode:
                for key, value in new_attributes.items():
                    setattr(item, key, value)
                return True
        return False

    def delete_item(self, barcode):
        for i, item in enumerate(self.items):
            if item.barcode == barcode:
                del self.items[i]
                return True
        return False

    def search_items(self, search_term):
        return [item for item in self.items if search_term.lower() in str(item).lower()]

    def find_near_expiry_items(self, threshold_days):
        """Here the argument is the term to search for in the item attributes
        Returns a list of Food items objects matching the search term"""

        from datetime import date
        "Import date module for date comparison"
        today = date.today()
        near_expiry = []
        for item in self.items:
            expiry_date = date.fromisoformat(item.expiry_date)
            days_remaining = (expiry_date-today).days
            if days_remaining <= threshold_days:
                near_expiry.append(item)
        return near_expiry
