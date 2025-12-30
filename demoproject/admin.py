from utils import load_items, save_items, print_table, SALES_FILE

def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Add Item")
        print("2. Update Item(s)")
        print("3. Delete Item")
        print("4. View Stock")
        print("5. View Sales")
        print("6. Back")

        choice = input("Enter choice: ")
        items = load_items()

        # ADD MULTIPLE ITEMS
        if choice == "1":
            print("Add products (type 'done' to finish)")
            while True:
                name = input("Item Name: ")
                if name.lower() == "done":
                    break
                price = float(input("Price: "))
                qty = int(input("Quantity: "))
                code = f"P{len(items)+1:03d}"
                items[code] = {
                    "name": name,
                    "price": price,
                    "qty": qty
                }
                print(f"Added {name} with code {code}")

            save_items(items)
            print("All items saved successfully!")

        # UPDATE MULTIPLE ITEMS (DONE OPTION)
        elif choice == "2":
            print("Update products (type 'done' to finish)")
            while True:
                code = input("Enter Product Code: ").strip()
                if code.lower() == "done":
                    break
                if code in items:
                    print(f"Current Price: Rs.{items[code]['price']}")
                    print(f"Current Quantity: {items[code]['qty']}")

                    price_input = input("Enter New Price (leave blank to keep old): ").strip()
                    qty_input = input("Enter New Quantity (leave blank to keep old): ").strip()

                    if price_input:
                        try:
                            items[code]["price"] = float(price_input)
                        except ValueError:
                            print("Invalid price input, keeping old price")

                    if qty_input:
                        try:
                            items[code]["qty"] = int(qty_input)
                        except ValueError:
                            print("Invalid quantity input, keeping old quantity")

                    print(f"Item {items[code]['name']} updated successfully!")
                else:
                    print("Invalid Product Code")

            save_items(items)
            print("All updates saved successfully!")

        # DELETE MULTIPLE ITEMS
        elif choice == "3":
            print("Delete products (type 'done' to finish)")
            while True:
                code = input("Enter Product Code: ").strip()
                if code.lower() == "done":
                    break
                if code in items:
                    print(f"Deleted {items[code]['name']}")
                    del items[code]
                else:
                    print("Invalid Product Code")

            save_items(items)
            print("Delete operation completed!")

        # VIEW STOCK
        elif choice == "4":
            headers = ["Code", "Item", "Price", "Quantity"]
            rows = []
            for c, d in items.items():
                rows.append([c, d["name"], d["price"], d["qty"]])
            print_table(headers, rows)

        # VIEW SALES
        elif choice == "5":
            headers = ["Item", "Qty Sold", "Total"]
            rows = []
            try:
                with open(SALES_FILE, "r") as f:
                    for line in f:
                        rows.append(line.strip().split(","))
                print_table(headers, rows)
            except FileNotFoundError:
                print("No sales data available")

        elif choice == "6":
            break
