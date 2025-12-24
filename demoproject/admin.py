
from utils import load_items, save_items, record_sale, ITEM_FILE, SALES_FILE

def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. View Stock")
        print("5. View Sales")
        print("6. Back to Main Menu")
        choice = input("Enter choice: ")

        items = load_items()

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter price: "))
            qty = int(input("Enter quantity: "))
            items[name] = {"price": price, "qty": qty}
            save_items(items)
            print("Item added successfully!")

        elif choice == "2":
            name = input("Enter item name to update: ")
            if name in items:
                price = float(input("Enter new price: "))
                qty = int(input("Enter new quantity: "))
                items[name] = {"price": price, "qty": qty}
                save_items(items)
                print("Item updated!")
            else:
                print("Item not found.")

        elif choice == "3":
            name = input("Enter item name to delete: ")
            if name in items:
                del items[name]
                save_items(items)
                print("Item deleted!")
            else:
                print("Item not found.")

        elif choice == "4":
            print("\n--- STOCK ---")
            for name, data in items.items():
                print(f"{name} - Price: {data['price']} - Qty: {data['qty']}")

        elif choice == "5":
            print("\n--- SALES RECORD ---")
            try:
                with open(SALES_FILE, "r") as f:
                    print(f.read())
            except FileNotFoundError:
                print("No sales yet.")

        elif choice == "6":
            break
        else:
            print("Invalid choice!")
