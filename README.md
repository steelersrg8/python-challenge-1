## **Requirements**
Order System (54 points)
An order list is initialized. (2 points)

User is prompted for their menu item selection and it's saved as a variable menu_selection. (4 points)

User input menu_selection is checked as a number and an error is printed if it is not. (4 points)

menu_selection is converted to an integer. (2 points)

An if-else statement is used to check if menu_selection is in the menu_items keys, and an error is printed if it isn't. (4 points)

The item name of the customer's selection is extracted from the menu_items dictionary and stored as a variable. (4 points)

The customer is prompted for a quantity of their item selection and the value defaults to 1 if the customer does not input a valid number. (10 points)

The customer's selected item, price, and quantity are appended to the order list in dictionary format. (10 points)

A match-case statement is used to check if the customer would like to keep ordering, and performs the correct actions for y, n, and default cases. (10 points)

The match-case statement converts the use input to lowercase or uppercase before checking the case. (4 points)

## **Order Receipt (46 points)**
A for loop is used to loop through the order list. (10 points)

The value of each key in each order dictionary is saved as a variable. (6 points)

The number of formatting spaces are correctly calculated. (6 points)

Space strings are created using string multiplication. (4 points)

The customer's order is printed with the item name, price, and quantity. (6 points)

List comprehension is used to calculate the total price of the order. (10 points)

The total price of the order is printed to the screen. (4 points)
