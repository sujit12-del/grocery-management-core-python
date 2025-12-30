import datetime
from utils import load_items, save_items, record_sale, record_user_history, USER_HISTORY_FILE, print_table

def process_payment(total_amount):
    print("\n--- PAYMENT OPTIONS ---")
    print(f"Bill Amount: Rs.{total_amount}")
    print("1. Cash")
    print("2. UPI")
    print("3. Debit Card")
    print("4. Credit Card")

    choice = input("Choose payment method: ")

    if choice == "1":
        print("Payment Successful (Cash)")
        return "Cash"
    elif choice == "2":
        input("Enter UPI ID / Mobile: ")
        print("Payment Successful (UPI)")
        return "UPI"
    elif choice == "3":
        input("Enter Debit Card Last 4 Digits: ")
        input("Enter PIN: ")
        print("Payment Successful (Debit Card)")
        return "Debit Card"
    elif choice == "4":
        input("Enter Credit Card Last 4 Digits: ")
        input("Enter CVV: ")
        print("Payment Successful (Credit Card)")
        return "Credit Card"
    else:
        print("Invalid payment option")
        return None

def generate_bill(username, purchased_items, total_amount, payment_mode):
    filename = f"bill_{username}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(filename, "w") as f:
        f.write("========================================\n")
        f.write("           FERTILIZER SHOP BILL         \n")
        f.write("========================================\n")
        f.write(f"Customer: {username}\n")
        f.write(f"Date: {datetime.datetime.now().strftime('%d-%m-%Y')}\n")
        f.write("----------------------------------------\n")
        f.write(f"{'S.No':<5} {'Item':<20} {'Qty':<5} {'Amount':<10}\n")
        f.write("----------------------------------------\n")
        
        for i, (item, data) in enumerate(purchased_items.items(), start=1):
            f.write(f"{i:<5} {item:<20} {data['qty']:<5} Rs.{data['price']:<10}\n")
        
        f.write("----------------------------------------\n")
        f.write(f"{'Total Amount':<30} Rs.{total_amount}\n")
        f.write(f"{'Payment Mode':<30} {payment_mode}\n")
        f.write("Status: SUCCESS\n")
        f.write("========================================\n")
        f.write("       Thank you for shopping with us!  \n")
        f.write("========================================\n")

    print(f"\nBill Generated: {filename}\n")


def user_menu(username):
    while True:
        print(f"\n--- USER MENU ({username}) ---")
        print("1. View Items")
        print("2. Purchase Items")
        print("3. View Purchase History")
        print("4. Back")

        choice = input("Enter choice: ")
        items = load_items()

        
        if choice == "1":
            headers = ["No", "Item", "Price", "Stock"]
            rows = []
            item_keys = list(items.keys())

            for i, code in enumerate(item_keys, start=1):
                d = items[code]
                rows.append([i, d["name"], d["price"], d["qty"]])

            print_table(headers, rows)

        
        elif choice == "2":
            purchased_items = {}
            total_amount = 0
            item_keys = list(items.keys())

            
            headers = ["No", "Item", "Price", "Stock"]
            rows = []
            for i, code in enumerate(item_keys, start=1):
                d = items[code]
                rows.append([i, d["name"], d["price"], d["qty"]])
            print_table(headers, rows)

            while True:
                choice_item = input("Enter Item No / Name (or 'done'): ").strip()
                if choice_item.lower() == "done":
                    break

                selected_code = None

                if choice_item.isdigit():
                    index = int(choice_item) - 1
                    if 0 <= index < len(item_keys):
                        selected_code = item_keys[index]
                else:
                    for code, d in items.items():
                        if d["name"].lower() == choice_item.lower():
                            selected_code = code
                            break

                if not selected_code:
                    print("Invalid selection")
                    continue

                
                qty_input = input("Enter Quantity: ").strip()
                if not qty_input.isdigit() or int(qty_input) <= 0:
                    print("Invalid quantity")
                    continue

                qty = int(qty_input)
                item = items[selected_code]

                if qty > item["qty"]:
                    print("Not enough stock")
                    continue

                total = qty * item["price"]
                item["qty"] -= qty
                save_items(items)

                record_sale(item["name"], qty, total)
                record_user_history(username, item["name"], qty, total)

                purchased_items[item["name"]] = {"qty": qty, "price": total}
                total_amount += total

                print(f"Added {qty} x {item['name']}")

            if purchased_items:
                payment_mode = process_payment(total_amount)
                if payment_mode:
                    generate_bill(username, purchased_items, total_amount, payment_mode)

        
        elif choice == "3":
            headers = ["Item", "Qty", "Total"]
            rows = []
            try:
                with open(USER_HISTORY_FILE, "r") as f:
                    for line in f:
                        user, item, qty, total = line.strip().split(",")
                        if user == username:
                            rows.append([item, qty, total])
                print_table(headers, rows)
            except FileNotFoundError:
                print("No history found")

        elif choice == "4":
            break
