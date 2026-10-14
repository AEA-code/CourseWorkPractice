'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# Café menu with fixed prices
menu_items = {
    "Latte": 4.00,
    "Croissant": 4.00,
    "Sandwich": 4.00,
    "Cheesecake": 4.00,
    "Tea": 4.00,
    "Coffee": 4.00,
    "Muffin": 4.00,
    "Chocolate Cake": 4.00
}

print(menu_items)

# Input: customer information
customer_name = input("Enter your name: ")
total = 0
total_quantity = 0

while True:
    customer_purchase = input("Enter your menu item: ").title()

    if customer_purchase in menu_items:
        quantity_purchase = int(input("Enter quantity: "))

        price = menu_items[customer_purchase]
        item_cost = price * quantity_purchase

        # Add item cost and quantity to the running totals
        total += item_cost
        total_quantity += quantity_purchase

        print(f"{quantity_purchase} {customer_purchase}(s) added to your order.")
    else:
        print(f"Sorry, {customer_purchase} is not available on the menu.")

    # Ask customer if they want to purchase another item
    print("\nWould you like to purchase another item?")
    print("1. Yes")
    print("2. No")

    choice = input("Enter your choice (1/yes or 2/no): ").strip().lower()

    if choice in ("1", "yes"):
        continue
    elif choice in ("2", "no"):
        print("Purchasing closed.")
        break
    else:
        print("Invalid choice. Purchasing closed.")
        break

# Final output
print(
    f"\nCustomer {customer_name} bought "
    f"{total_quantity} items. "
    f"Total cost: ${total:.2f}"
)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    