# This will calculate expenses and expenditures

while True:
    try:
        # Ask for monthly allowence and expenses in different categories
        income = float(input("What is your monthly income? $"))
        snacks = float(input("How much was spent on snacks? $"))
        clothes = float(input("How much was spent on clothes? $"))
        entertainment = float(input("How much was spent on entertainment? $"))
        break
    except ValueError:
        print("Please enter a proper number.")

# Calculate total expenses and remaining balance
total_expenses = snacks + clothes + entertainment
remaining_balance = income - total_expenses

# Display Results
print(f"Your income is: ${income:.2f}")
print(f"Your total expenses are: ${total_expenses:.2f}")
print(f"Your remaining balance is: ${remaining_balance:.2f}")

# Conditional message based on balance
if remaining_balance <= 0:
    print("You have overspent and now have nothing.")
elif remaining_balance <=0.1 * income:
    print("Good job, you only still have 10% of your income left.")

