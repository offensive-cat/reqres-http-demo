import reqres_http_demo as http_demo

def menu():
  print("\n1. Display all users")
  print("2. Get a user by ID")
  print("3. Register a new user")
  print("4. Login a user")
  print("5. Edit a user's details")
  print("6. Delete a user")
  print("7. Exit")

while True:
  menu()
  choice = input("Enter your choice: ")
  if choice == '1':
    http_demo.user_data()
  elif choice == '2':
    user_id = int(input("Enter the user ID: "))
    http_demo.get_user(user_id)
  elif choice == '3':
    email = input("Enter email: ")
    password = input("Enter password: ")
    http_demo.registration(email, password)
  elif choice == '4':
    email = input("Enter email: ")
    password = input("Enter password: ")
    http_demo.login(email, password)
  elif choice == '5':
    user_id = input("Enter the user ID: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    http_demo.edit_user(user_id, first_name, last_name, email, password)
  elif choice == '6':
    user_id = input("Enter the user ID: ")
    http_demo.delete_user(user_id)
  elif choice == '7':
    break
  
menu()
