# user.py
import datetime
from utils import load_items, save_items, record_sale, record_user_history, USER_HISTORY_FILE

def process_payment(total_amount):
    print("\n--- PAYMENT OPTIONS ---")
    print(f"Bill Amount: Rs.{total_amount}")
    print("1. Cash")
    print("2. UPI")
    print("3. Debit Card")
    print("4. Credit Card")

    choice = input("Choose payment method: ")

    if choice == "1":
        print(f"Cash received: Rs.{total_amount}")
        print("Payment Successful ✅")
        return "Cash"

    elif choice == "2":
        input("Enter UPI ID / Mobile Number: ")
        print(f"Processing Rs.{total_amount} via UPI...")
        print("Payment Successful ✅")
        return "UPI"

    elif choice == "3":
        input("Enter Debit Card Number (last 4 digits): ")
        input("Enter PIN: ")
        print("Processing Debit Card payment...")
        print("Payment Successful ✅")
        return "Debit Card"

    elif choice == "4":
        input("Enter Credit Card Number (last 4 digits): ")
        input("Enter CVV: ")
        print("Processing Credit Card payment...")
        print("Payment Successful ✅")
        return "Credit Card"

    else:
        print("Invalid payment option!")
        return None


def generate_bill(username, purchased_items, total_amount, payment_mode):
    bill_filename = f"bill_{username}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(bill_filename, "w") as f:
        f.write("=== FERTILIZER SHOP BILL ===\n")
        f.write(f"Customer: {username}\n")
        f.write(f"Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        f.write("----------------------------\n")
        f.write("Item\tQty\tPrice\n")
        f.write("----------------------------\n")

        for item, details in purchased_items.items():
            f.write(f"{item}\t{details['qty']}\tRs.{details['price']}\n")

        f.write("----------------------------\n")
        f.write(f"Total Amount: Rs.{total_amount}\n")
        f.write(f"Payment Mode: {payment_mode}\n")
        f.write("Payment Status: SUCCESS\n")
        f.write("Thank you for shopping with us!\n")

    print(f"\nBill generated: {bill_filename}")


def user_menu(username):
    while True:
        print(f"\n--- USER MENU ({username}) ---")
        print("1. View Items")
        print("2. Purchase Item")
        print("3. View Purchase History")
        print("4. Back to Main Menu")
        choice = input("Enter choice: ")

        items = load_items()

        if choice == "1":
            print("\n--- ITEMS AVAILABLE ---")
            for name, data in items.items():
                print(f"{name} - Price: {data['price']} - Qty: {data['qty']}")

        elif choice == "2":
            purchased_items = {}
            total_amount = 0

            while True:
                name = input("Enter item name (or 'done' to finish): ").strip()
                if name.lower() == "done":
                    break

                if name in items and items[name]['qty'] > 0:
                    qty = int(input("Enter quantity: "))
                    if qty <= items[name]['qty']:
                        total = qty * items[name]['price']
                        items[name]['qty'] -= qty
                        save_items(items)
                        record_sale(name, qty, total)
                        record_user_history(username, name, qty, total)

                        purchased_items[name] = {"qty": qty, "price": total}
                        total_amount += total
                        print(f"Added {qty} x {name}")
                    else:
                        print("Not enough stock.")
                else:
                    print("Item not available.")

            if purchased_items:
                payment_mode = process_payment(total_amount)
                if payment_mode:
                    generate_bill(username, purchased_items, total_amount, payment_mode)
                else:
                    print("Payment Failed ❌")
            else:
                print("No items purchased.")

        elif choice == "3":
            print("\n--- PURCHASE HISTORY ---")
            try:
                with open(USER_HISTORY_FILE, "r") as f:
                    for line in f:
                        user, item, qty, total = line.strip().split(",")
                        if user == username:
                            print(f"{item} - Qty: {qty} - Total: {total}")
            except FileNotFoundError:
                print("No purchase history found.")

        elif choice == "4":
            break
        else:
            print("Invalid choice!")
