import csv
from datetime import date


class FileManager:
    def __init__(self, filename):
        """
        Initialize FileManager object.

        Args:
        - filename (str): Filename of the CSV file.
        """
        self.filename = filename

    def read_from_csv(self):
        """
        Read inventory data from CSV file and return a list of items.

        Returns:
        - list: List of dictionaries representing items.
        """
        items = []
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    expiry_date = date.fromisoformat(row['expiry_date']) if row['expiry_date'] else None
                    item = {'name': row['name'], 'category': row['category'], 'quantity': int(row['quantity']),
                            'barcode': row['barcode'], 'expiry_date': expiry_date}
                    items.append(item)
        except (IOError, FileNotFoundError):
            print(f"Error reading from CSV file: {self.filename}")
        return items

    def write_to_csv(self, items):
        """
        Write inventory data to CSV file.

        Args:
        - items (list): List of dictionaries representing items to be written.
        """
        try:
            with open(self.filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['name', 'category', 'quantity', 'barcode', 'expiry_date'])
                writer.writeheader()
                for item in items:
                    expiry_str = item['expiry_date'].isoformat() if item['expiry_date'] else None
                    writer.writerow({'name': item['name'], 'category': item['category'], 'quantity': item['quantity'],
                                     'barcode': item['barcode'], 'expiry_date': expiry_str})
        except (IOError, PermissionError):
            print(f"Error writing to CSV file: {self.filename}")
