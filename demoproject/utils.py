

ITEM_FILE = "items.txt"
SALES_FILE = "sales.txt"
USER_HISTORY_FILE = "user_history.txt"

def load_items():
    items = {}
    try:
        with open(ITEM_FILE, "r") as f:
            for line in f:
                name, price, qty = line.strip().split(",")
                items[name] = {"price": float(price), "qty": int(qty)}
    except FileNotFoundError:
        pass
    return items

def save_items(items):
    with open(ITEM_FILE, "w") as f:
        for name, data in items.items():
            f.write(f"{name},{data['price']},{data['qty']}\n")

def record_sale(item_name, qty, total):
    with open(SALES_FILE, "a") as f:
        f.write(f"{item_name},{qty},{total}\n")

def record_user_history(username, item_name, qty, total):
    with open(USER_HISTORY_FILE, "a") as f:
        f.write(f"{username},{item_name},{qty},{total}\n")
