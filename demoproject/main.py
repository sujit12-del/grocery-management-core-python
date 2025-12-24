
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
        role = input("Enter choice: ")

        if role == "1":
            if login_admin():
                admin_menu()

        elif role == "2":
            username = login_user()
            if username:
                user_menu(username)

        elif role == "3":
            register_admin()

        elif role == "4":
            register_user()

        elif role == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
