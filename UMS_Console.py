class UserManagementSystem:
    def __init__(self):
        self.users = []

    # Creating User Info 
    def create_user(self):
        name = input("Enter User name: ")
        while True:
          email = input("Enter user email: ")
          if "@" not in email:
            print("Email address must contain '@'. Please try again.")
          else:
            break
        age = input("Enter User age: ")
        address = input("Enter User address: ")
        self.users.append({"name": name, "email": email, "age": age, 								"address" : address})
        print("User created successfully. ")
        

  # Listing Users
    def list_users(self):
        if not self.users:
            print("No users found.")
        else:
            for index, user in enumerate(self.users):
                print(f"User {index + 1}:")
                print(f"Name: {user['name']}")
                print(f"Email: {user['email']}")
                print(f"Age: {user['age']}")
                print(f"Address: {user['address']}")
                print("")

    # Editing Users Info 
    def edit_user(self):
        if not self.users:
            print("No users found.")
        else:
            self.list_users()
            user_index = int(input("Enter the user number you want to 									edit: ")) – 1

            if user_index < 0 or user_index >= len(self.users):
                print("Invalid user number.")
                return
            user = self.users[user_index]

            name = input(f"Enter new name for {user['name']}: ")


            while True:
              email = input(f"Enter new email for {user['email']}: ")
              if "@" not in email:
                print("Email address must contain '@'. Please try 											again.")
              else:
                break

            age = input(f"Enter new age for {user['age']}: ")
            address = input(f"Enter new address for {user['address']}: ")

            user['name'] = name
            user['email'] = email
            user['age'] = age
            user['address'] = address
            print("User information updated successfully.")
            

     # Deleting Users Info 
    def delete_user(self):
        if not self.users:
            print("No users found.")
        else:
            self.list_users()
            user_index = int(input("Enter the user number you want to 							delete: ")) - 1
            if user_index < 0 or user_index >= len(self.users):
                print("Invalid user number.")
                return
            del self.users[user_index]
            print("User deleted successfully.")
            

    def run(self):
        while True:
            print("User Management System")
            print("1. Create User")
            print("2. List Users")
            print("3. Edit User")
            print("4. Delete User")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_user()
            elif choice == '2':
                self.list_users()
            elif choice == '3':
                self.edit_user()
            elif choice == '4':
                self.delete_user()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")
            

if __name__ == "__main__":
    user_management_system = UserManagementSystem()
    user_management_system.run()



