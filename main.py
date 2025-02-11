def option_one():
    print("You selected Option 1.")

def option_two():
    print("You selected Option 2.")

def option_three():
    print("You selected Option 3.")

def exit_program():
    print("Exiting program.")
    exit()

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Run Option 1")
        print("2. Run Option 2")
        print("3. Run Option 3")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            option_one()
        elif choice == "2":
            option_two()
        elif choice == "3":
            option_three()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()

