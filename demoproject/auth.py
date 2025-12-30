ADMIN_CRED_FILE = "admin_credentials.txt"
USER_CRED_FILE = "user_credentials.txt"

def read_credentials(file):
    creds = {}
    try:
        with open(file) as f:
            for line in f:
                u, p = line.strip().split(",")
                creds[u] = p
    except FileNotFoundError:
        pass
    return creds

def write_credentials(file, u, p):
    with open(file, "a") as f:
        f.write(f"{u},{p}\n")

def register_admin():
    u = input("Admin ID: ")
    p = input("Password: ")
    if u in read_credentials(ADMIN_CRED_FILE):
        print("Admin exists")
    else:
        write_credentials(ADMIN_CRED_FILE, u, p)
        print("Admin registered")

def register_user():
    u = input("User ID: ")
    p = input("Password: ")
    if u in read_credentials(USER_CRED_FILE):
        print("User exists")
    else:
        write_credentials(USER_CRED_FILE, u, p)
        print("User registered")

def login_admin():
    u = input("Admin ID: ")
    p = input("Password: ")
    return read_credentials(ADMIN_CRED_FILE).get(u) == p

def login_user():
    u = input("User ID: ")
    p = input("Password: ")
    return u if read_credentials(USER_CRED_FILE).get(u) == p else None
