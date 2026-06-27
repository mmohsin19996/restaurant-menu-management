# Restaurant Menu Management System

menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80
}

print("========== Welcome to Python Restaurant ==========")
print("Menu")
print("---------------------------------")

for item, price in menu.items():
    print(f"{item} : Rs.{price}")

print("---------------------------------")

order_total = 0

while True:
    item = input("\nEnter the item you want to order: ")

    if item in menu:
        order_total += menu[item]
        print(f"{item} has been added to your order.")
    else:
        print("Sorry! This item is not available.")

    another_order = input("Do you want to order another item? (yes/no): ").lower()

    if another_order != "yes":
        break

print("\n========== Bill ==========")
print(f"Total Amount = Rs.{order_total}")
print("Thank You! Visit Again ??")