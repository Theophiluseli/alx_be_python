# Function to display the menu
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main function to manage the shopping list
def main():
    shopping_list = []  # Initialize the shopping list
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Prompt for an item to add to the list
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item cannot be empty.")

        elif choice == '2':
            # Prompt for an item to remove from the list
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("\nYour shopping list is empty.")

        elif choice == '4':
            # Exit the loop and terminate the program
            print("Goodbye!")
            break

        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")
# Entry point of the script
if __name__ == "__main__":
    main()
