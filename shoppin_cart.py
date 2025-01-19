#!/usr/bin/env python3
def add_to_cart():
    """Simulates a shopping cart program."""
    cart = {} 
    total_cost = 0

    while True:
        item_name = input("Enter item name (or 'done' to finish): ").strip()
        if item_name.lower() == 'done':
            break
        if item_name in cart:
            print(f"{item_name} is already in the cart. Skipping duplicate.")
            continue

        try:
            price = float(input("Enter item price: ").strip())
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue

        try:
            discount = float(input("Enter discount (as a percentage, e.g., 10 for 10%): ").strip())
            if discount < 0 or discount > 100:
                print("Invalid discount. Please enter a value between 0 and 100.")
                continue
        except ValueError:
            print("Invalid discount. Please enter a number.")
            continue
        final_price = price * (1 - discount / 100)
 
        cart[item_name] = final_price
        total_cost += final_price
        print(f"{item_name} added to cart at ${final_price:.2f}.")

    print("\nCart Summary:")
    for item, price in cart.items():
        print(f"- {item}: ${price:.1f}")
    print(f"Total Cost: ${total_cost:.1f}")

# Runs the function
add_to_cart()

