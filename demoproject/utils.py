ITEM_FILE = "items.txt"
SALES_FILE = "sales.txt"
USER_HISTORY_FILE = "user_history.txt"

def load_items():
    items = {}
    try:
        with open(ITEM_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, price, qty = parts
                    code = f"P{len(items)+1:03d}"
                else:
                    code, name, price, qty = parts

                items[code] = {
                    "name": name,
                    "price": float(price),
                    "qty": int(qty)
                }
    except FileNotFoundError:
        pass
    return items

def save_items(items):
    with open(ITEM_FILE, "w") as f:
        for code, data in items.items():
            f.write(f"{code},{data['name']},{data['price']},{data['qty']}\n")

def record_sale(item, qty, total):
    with open(SALES_FILE, "a") as f:
        f.write(f"{item},{qty},{total}\n")

def record_user_history(user, item, qty, total):
    with open(USER_HISTORY_FILE, "a") as f:
        f.write(f"{user},{item},{qty},{total}\n")

def print_table(headers, rows):
    widths = [len(h) for h in headers]
    for row in rows:
        for i, col in enumerate(row):
            widths[i] = max(widths[i], len(str(col)))

    line = "+" + "+".join(["-" * (w + 2) for w in widths]) + "+"
    print(line)
    print("| " + " | ".join(headers[i].ljust(widths[i]) for i in range(len(headers))) + " |")
    print(line)

    for row in rows:
        print("| " + " | ".join(str(row[i]).ljust(widths[i]) for i in range(len(row))) + " |")
    print(line)
