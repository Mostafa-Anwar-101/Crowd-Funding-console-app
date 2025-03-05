from auth import register, login
from projects import create_project, view_projects, edit_project, delete_project

def main():
    user_email = None

    while True:
        if user_email:
            print("\nWelcome! Choose an option:")
            print("1. Create Project")
            print("2. View Projects")
            print("3. Edit Project")
            print("4. Delete Project")
            print("5. Logout")
        else:
            print("\n1. Register")
            print("2. Login")
            print("3. Exit")

        choice = input("Choose an option: ")

        if not user_email:
            if choice == "1":
                register()
            elif choice == "2":
                user_email = login()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        else:
            if choice == "1":
                create_project(user_email)
            elif choice == "2":
                view_projects()
            elif choice == "3":
                edit_project(user_email)
            elif choice == "4":
                delete_project(user_email)
            elif choice == "5":
                print("Logged out.")
                user_email = None
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
