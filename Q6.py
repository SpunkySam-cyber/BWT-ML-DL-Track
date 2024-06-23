def update_inventory(inventory_dict, item, quantity):
    current_quantity = inventory_dict.get(item, 0)
    new_quantity = current_quantity + quantity
    
    if new_quantity < 0:
        new_quantity = 0
    
    inventory_dict[item] = new_quantity
    return inventory_dict

def main():

    inventory = {
        'apple': 10,
        'banana': 15,
        'orange': 20,
        'mango': 8,
        'pear': 12
    }

    for i in range(3):
        print(f"\nInventory: {inventory}")
        item = input("Enter item to update: ").strip().lower()
        quantity = int(input("Enter quantity to add/remove: "))
        
        inventory = update_inventory(inventory, item, quantity)
    
    print("\nUpdated Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

if __name__ == "__main__":
    main()
