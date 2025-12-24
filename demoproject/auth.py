

ADMIN_CRED_FILE = "admin_credentials.txt"
USER_CRED_FILE = "user_credentials.txt"

def read_credentials(file_path):
    creds = {}
    try:
        with open(file_path, "r") as f:
            for line in f:
                username, password = line.strip().split(",")
                creds[username] = password
    except FileNotFoundError:
        pass
    return creds

def write_credentials(file_path, username, password):
    with open(file_path, "a") as f:
        f.write(f"{username},{password}\n")

def register_admin():
    username = input("Enter new Admin ID: ")
    password = input("Enter new Admin Password: ")
    creds = read_credentials(ADMIN_CRED_FILE)

    if username in creds:
        print("Admin already exists!")
    else:
        write_credentials(ADMIN_CRED_FILE, username, password)
        print("Admin registered successfully!")

def register_user():
    username = input("Enter new User ID: ")
    password = input("Enter new User Password: ")
    creds = read_credentials(USER_CRED_FILE)

    if username in creds:
        print("User already exists!")
    else:
        write_credentials(USER_CRED_FILE, username, password)
        print("User registered successfully!")

def login_admin():
    username = input("Enter Admin ID: ")
    password = input("Enter Admin Password: ")
    creds = read_credentials(ADMIN_CRED_FILE)

    if username in creds and creds[username] == password:
        return True
    else:
        print("Invalid Admin credentials!")
        return False

def login_user():
    username = input("Enter User ID: ")
    password = input("Enter User Password: ")
    creds = read_credentials(USER_CRED_FILE)

    if username in creds and creds[username] == password:
        return username
    else:
        print("Invalid User credentials!")
        return None
