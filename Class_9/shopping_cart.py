cart = []

def take_cart():
    cart = []

def add_item(item, cart):
    cart.append(item)
    print(f"{item} has been added in the cart.")

def remove_item(item, cart):
    cart.remove(item)
    print(f"{item} has been removed from the cart.")

def check_out(cart):
    print(f"You have parchased the following items: ")
    print(item for item in cart)
    # for item in cart:
    #     print(item)

def search_item(item, cart):
    if item in cart:
        print(f"{item} already exist in the cart!")
    else:
        print(f"{item} doesn't exist in the cart!")


# take_cart()
# add_item("Banana", cart)
# add_item("Mango", cart)
# add_item("Apple", cart)
# add_item("Pen", cart)
# add_item("Iphone", cart)

# remove_item("Iphone", cart)

# check_out(cart)


is_cart = input("Do you want to take a cart?: ")
if is_cart == "No":
    pass
else:
    take_cart()

    item_input = input("Enter the item you want to add:(Enter 'q' to exit) ")
    add_item(item_input, cart)
    while item_input.lower() != "q":
        item_input = input("Enter the item you want to add:(Enter 'q' to exit) ")
        add_item(item_input, cart)

    item_input = input("Enter the item you want to remove:(Enter 'q' to exit) ")
    while item_input.lower() != "q":
        remove_item(item_input, cart)
        item_input = input("Enter the item you want to remove:(Enter 'q' to exit) ")
        remove_item(item_input, cart)

    item_input = input("Enter the item you want to remove:(Enter 'q' to exit) ")
    check_out(cart)