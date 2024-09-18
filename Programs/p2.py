# Implement a simple shopping cart program using an array. Create functions to add items, remove items, and update quantities using array methods. Print the cart's contents after each operation.

# Shopping Cart Program

# Initial shopping cart (empty)
shopping_cart = []

# Function to add an item to the cart
def add_item(item_name, quantity):
    # Check if item already exists in the cart
    for item in shopping_cart:
        if item['name'] == item_name:
            item['quantity'] += quantity
            print(f"Updated {item_name}'s quantity to {item['quantity']}.")
            return
    # If item does not exist, add it as a new item
    shopping_cart.append({'name': item_name, 'quantity': quantity})
    print(f"Added {item_name} to the cart with quantity {quantity}.")

# Function to remove an item from the cart
def remove_item(item_name):
    for item in shopping_cart:
        if item['name'] == item_name:
            shopping_cart.remove(item)
            print(f"Removed {item_name} from the cart.")
            return
    print(f"{item_name} not found in the cart.")

# Function to update the quantity of an item
def update_quantity(item_name, new_quantity):
    for item in shopping_cart:
        if item['name'] == item_name:
            if new_quantity > 0:
                item['quantity'] = new_quantity
                print(f"Updated {item_name}'s quantity to {new_quantity}.")
            else:
                remove_item(item_name)
            return
    print(f"{item_name} not found in the cart.")

# Function to print the current cart contents
def print_cart():
    if shopping_cart:
        print("\nShopping Cart Contents:")
        for item in shopping_cart:
            print(f"- {item['name']}: {item['quantity']}")
    else:
        print("\nYour shopping cart is empty.")

# Example usage
add_item("Apple", 3)
print_cart()

add_item("Banana", 2)
print_cart()

update_quantity("Apple", 5)
print_cart()

remove_item("Banana")
print_cart()

remove_item("Orange")  # Trying to remove an item that doesn't exist



# ---------- Example OutPut --------------------

# Added Apple to the cart with quantity 3.

# Shopping Cart Contents:
# - Apple: 3

# Added Banana to the cart with quantity 2.

# Shopping Cart Contents:
# - Apple: 3
# - Banana: 2

# Updated Apple's quantity to 5.

# Shopping Cart Contents:
# - Apple: 5
# - Banana: 2

# Removed Banana from the cart.

# Shopping Cart Contents:
# - Apple: 5

# Orange not found in the cart.

# Shopping Cart Contents:
# - Apple: 5
