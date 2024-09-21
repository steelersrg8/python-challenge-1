# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("\nFrom which menu would you like to order?")

    # Display the menu categories
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    # Get the customer's input for category
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a valid number for category
    if menu_category.isdigit() and int(menu_category) in menu_items:
        menu_category_name = menu_items[int(menu_category)]
        print(f"\nYou selected {menu_category_name}.")

        # Print out the options in the selected category
        print(f"What {menu_category_name} item would you like to order?")
        i = 1
        menu_items = {}
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")

        # Display items in the selected category
        for key, value in menu[menu_category_name].items():
            if isinstance(value, dict):  # Handle sub-menus (like pizza or burgers)
                for sub_key, sub_value in value.items():
                    item_name = f"{key} - {sub_key}"
                    num_item_spaces = 24 - len(item_name)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {item_name}{item_spaces} | ${sub_value:.2f}")
                    menu_items[i] = {"Item name": item_name, "Price": sub_value}
                    i += 1
            else:  # Handle regular items
                num_item_spaces = 24 - len(key)
                item_spaces = " " * num_item_spaces
                print(f"{i}      | {key}{item_spaces} | ${value:.2f}")
                menu_items[i] = {"Item name": key, "Price": value}
                i += 1

        # 2. Ask customer to input menu item number
        item_number = input("\nSelect the item number: ")

        # 3. Check if the customer input is a valid item number
        if item_number.isdigit() and int(item_number) in menu_items:
            selected_item = menu_items[int(item_number)]

            # Ask for quantity
            quantity = input(f"How many {selected_item['Item name']} would you like to order? ")

            # Default quantity to 1 if not a valid number
            if not quantity.isdigit():
                quantity = 1
            else:
                quantity = int(quantity)

            # 4. Add the item to the order list
            order_list.append({
                "Item name": selected_item["Item name"],
                "Price": selected_item["Price"],
                "Quantity": quantity
            })

            print(f"\n{quantity} {selected_item['Item name']}(s) added to your order.")

        else:
            print("Invalid selection. Please choose a valid item number.")
    else:
        print("Invalid selection. Please choose a valid menu category.")

    # 5. Ask the customer if they would like to order anything else
    keep_ordering = input("\nWould you like to keep ordering? (Y)es or (N)o: ").lower()
    if keep_ordering == "n":
        place_order = False

# Print out the customer's order
print("\nThis is what we are preparing for you:\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the order list
for item in order_list:
    # 7. Store the dictionary items as variables
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 24 - len(item_name)
    item_spaces = " " * num_item_spaces

    # 9. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces} | ${price:.2f} | {quantity}")

# 10. Calculate the total cost
total_cost = sum(item["Price"] * item["Quantity"] for item in order_list)

# 11. Print the total cost
print(f"\nTotal cost of your order: ${total_cost:.2f}")
print("Thank you for ordering with us!")
