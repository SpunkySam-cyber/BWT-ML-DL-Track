class FoodItem:
    def __init__(self, name, category, quantity, barcode, expiry_date=None):
        """
        Initialize a FoodItem object.

        Args:
        - name (str): Name of the food item.
        - category (str): Category of the food item.
        - quantity (int): Quantity of the food item.
        - barcode (str): Barcode of the food item.
        - expiry_date (date): Optional, expiry date of the food item.
        """
        self.name = name
        self.category = category
        self.quantity = quantity
        self.barcode = barcode
        self.expiry_date = expiry_date
    def __str__(self):
        return f"Name: {self.name} \nCategory: {self.category} \nQuantity : {self.quantity} \nBarcode: {self.barcode} \nExpiry Date :{self.expiry_date}"


