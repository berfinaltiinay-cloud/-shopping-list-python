shopping_list = []

while True:
    print("\n--- Shopping List ---")
    print("1. Add item")
    print("2. Show list")
    print("3. Remove item")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter an item: ")
        shopping_list.append(item)
        print(item, "added to the list.")

    elif choice == "2":
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            print("\nYour Shopping List:")
            for item in shopping_list:
                print("-", item)

    elif choice == "3":
        item = input("Enter the item you want to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed from the list.")
        else:
            print("This item is not on the list.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
