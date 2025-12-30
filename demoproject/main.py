from admin import admin_menu
from user import user_menu
from auth import register_admin, register_user, login_admin, login_user

def main():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Register Admin")
        print("4. Register User")
        print("5. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            if login_admin():
                admin_menu()
        elif ch == "2":
            u = login_user()
            if u:
                user_menu(u)
        elif ch == "3":
            register_admin()
        elif ch == "4":
            register_user()
        elif ch == "5":
            break

if __name__ == "__main__":
    main()
