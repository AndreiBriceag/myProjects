
snacks = {
    "Popcorn": 3.40,
    "Chocolate": 1.25,
    "Soda": 2.70,
    "Nachos": 4.90,
    "Fries": 3.90
}

print(
      "Hello, Welcome to the Snacks Section!",
      "Here is our menu. What would you like?",
      "",
      "===== SNACK MENU =====",
      *[f"{snack} - ${price:.2f}" for snack, price in snacks.items()],
      "",
      sep="\n"
     )


ordering = 'yes'
total = 0
while ordering == 'yes':
    while (snack := input("Enter a snack: ").title()) not in snacks:
        print("Invalid choice!")

    while not (quantity := input("Enter a quantity: ")).isdigit() or int(quantity) < 0:
        print("Invalid number!")

    price = snacks[snack]
    total += price * int(quantity)

    while (ordering := input("Would you like to order another item? Enter 'yes' or 'no': ").lower()) not in ['yes', 'no']:
        print("Invalid choice!")


print(f"Your total is ${total:.2f}.")