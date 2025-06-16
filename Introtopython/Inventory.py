# Creating inventory list
inventory = [
    ["Apple", 50],
    ["Bananas", 30],
    ["Orange", 20],
    ["Milk", 15],
    ["Bread", 25]
]

# Showing all available items
def show_inventory():
    print("\n--- CURRENT INVENTORY ---")
    if len(inventory) == 0:
        print("No items in inventory!")
        return
    
    for i in range(len(inventory)):
        item = inventory[i][0]
        quantity = inventory[i][1]
        print(f"{i+1}. {item}: {quantity}")

# Adding more items to existing stock
def add_stock():
    name = input("Enter item name to add stock: ")
    
    for i in range(len(inventory)):
        if inventory[i][0].lower() == name.lower():
            try:
                amount = int(input(f"How many {name} to add? "))
                if amount > 0:
                    inventory[i][1] += amount
                    print(f" Added {amount} {name}. New total: {inventory[i][1]}")
                else:
                    print(" Please enter a positive number!")
                return
            except ValueError:
                print(" Please enter a valid number!")
                return
    
    print(f"{name} not found in inventory!")

# Removing items from stock
def remove_stock():
    name = input("Enter item name to remove stock: ")
    
    for i in range(len(inventory)):
        if inventory[i][0].lower() == name.lower():
            try:
                amount = int(input(f"How many {name} to remove? "))
                if amount > 0:
                    if inventory[i][1] >= amount:
                        inventory[i][1] -= amount
                        print(f" Removed {amount} {name}. Remaining: {inventory[i][1]}")
                    else:
                        print(f" Not enough {name}! Only have {inventory[i][1]}")
                else:
                    print(" Please enter a positive number!")
                return
            except ValueError:
                print(" Please enter a valid number!")
                return
    
    print(f" {name} not found in inventory!")

# Checking for low stock
def check_low_stock():
    print("\n--- LOW STOCK ALERT ---")
    found_low_stock = False
    
    for i in range(len(inventory)):
        if inventory[i][1] < 10:
            print(f" {inventory[i][0]}: only {inventory[i][1]} left")
            found_low_stock = True
    
    if not found_low_stock:
        print(" All items have good stock levels!")

# Adding completely new item
def add_new_item():
    name = input("Enter new item name: ").strip()
    
    # Check if name is empty
    if not name:
        print(" Item name cannot be empty!")
        return
    
    # Checking if item already exists
    for i in range(len(inventory)):
        if inventory[i][0].lower() == name.lower():
            print(f" {name} already exists! Use 'Add Stock' instead.")
            return
    
    try:
        quantity = int(input(f"Enter quantity for {name}: "))
        if quantity >= 0:
            inventory.append([name, quantity])
            print(f" Successfully added new item: {name} ({quantity})")
            print(f" Total items in inventory: {len(inventory)}")
        else:
            print(" Quantity cannot be negative!")
    except ValueError:
        print(" Please enter a valid number for quantity!")

# Searching for an item
def search_item():
    name = input("Enter item name to search: ")
    
    for i in range(len(inventory)):
        if inventory[i][0].lower() == name.lower():
            print(f" Found: {inventory[i][0]} - Quantity: {inventory[i][1]}")
            return
    
    print(f" {name} not found in inventory!")

# Main menu
def show_menu():
    print("\n" + "="*35)
    print(" INVENTORY MANAGEMENT SYSTEM")
    print("="*35)
    print("1. Show All Items")
    print("2. Add New Item")
    print("3. Add Stock to Existing Item")
    print("4. Remove Stock")
    print("5. Search for Item")
    print("6. Check Low Stock")
    print("7. Exit")
    print("-"*35)

# Main program loop
def main():
    print("Welcome to the Inventory Management System!")
    print(f"Starting with {len(inventory)} items in inventory.")
    
    while True:
        show_menu()
        
        try:
            choice = input("Choose an option (1-7): ").strip()
            
            if choice == "1":
                show_inventory()
            
            elif choice == "2":
                add_new_item()
            
            elif choice == "3":
                show_inventory()
                if len(inventory) > 0:
                    add_stock()
            
            elif choice == "4":
                show_inventory()
                if len(inventory) > 0:
                    remove_stock()
            
            elif choice == "5":
                search_item()
            
            elif choice == "6":
                check_low_stock()
            
            elif choice == "7":
                print(" Thank you for using the Inventory System!")
                print(f" Final inventory count: {len(inventory)} items")
                break
            
            else:
                print(" Invalid choice! Please choose 1-7.")
        
        except Exception as e:
            print(" Something went wrong! Please try again.")
        
        if choice != "7":
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()