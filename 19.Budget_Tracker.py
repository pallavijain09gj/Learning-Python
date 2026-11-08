
import math
import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


monthly_budget = None
expenses = []


def get_positive_amount(prompt):
    try:
        amount = float(input(prompt))
    except ValueError:
        print("Please enter a valid number")
        return None

    if not math.isfinite(amount) or amount <= 0:
        print("Amount must be greater than 0.")
        return None

    return amount


while True:
    print("\n===== MONTHLY BUDGET TRACKER =====")
    print("1. Set Monthly Budget")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Budget Summary")
    print("5. Exit")

    choice = input("\nEnter choice: ").strip()

    if choice == "1":
        budget = get_positive_amount("Enter monthly budget: ")
        if budget is not None:
            monthly_budget = budget
            print("Budget set successfully!")

    elif choice == "2":
        name = input("Expense name: ").strip()
        category = input("Category: ").strip()

        if not name or not category:
            print("Expense name and category cannot be empty.")
            continue

        amount = get_positive_amount("Amount: ")
        if amount is not None:
            expenses.append({
                "name": name,
                "category": category,
                "amount": amount,
            })
            print("Expense added successfully!")

    elif choice == "3":
        if not expenses:
            print("No expenses added yet.")
        else:
            print("\n===== EXPENSES =====")
            for number, expense in enumerate(expenses, start=1):
                print(
                    f"{number}. {expense['name']} "
                    f"({expense['category']}) - ₹{expense['amount']:.2f}"
                )

    elif choice == "4":
        if monthly_budget is None:
            print("Please set a monthly budget first.")
            continue

        total_spent = sum(expense["amount"] for expense in expenses)
        remaining = monthly_budget - total_spent
        status = "Within Budget" if remaining >= 0 else "Over Budget"

        print("\n===== BUDGET SUMMARY =====")
        print(f"Monthly Budget : ₹{monthly_budget:.2f}")
        print(f"Total Spent    : ₹{total_spent:.2f}")
        print(f"Remaining      : ₹{remaining:.2f}")
        print(f"Status         : {status}")

    elif choice == "5":
        print("Exiting Budget Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
