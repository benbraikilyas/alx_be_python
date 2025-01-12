def display_menu():
    """
    Display the menu of options for the shopping list manager.
    """
    print("\nShopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the shopping list")
    print("4. Exit")

def add_item(shopping_list):
    """
    Add an item to the shopping list.

    Args:
        shopping_list (list): The current shopping list.
    """
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the list.")
    else:
        print("Item cannot be empty.")

def remove_item(shopping_list):
    """
    Remove an item from the shopping list.

    Args:
        shopping_list (list): The current shopping list.
    """
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' is not in the shopping list.")

def view_list(shopping_list):
    """
    Display the current shopping list.

    Args:
        shopping_list (list): The current shopping list.
    """
    if shopping_list:
        print("\nCurrent Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")

def main():
    """
    Main function to run the shopping list manager.
    """
    shopping_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()
