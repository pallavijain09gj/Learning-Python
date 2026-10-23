import math
from datetime import date


data_file = "expenses.txt"


def read_expenses():
    expenses = []
    try:
        with open(data_file, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip() == "":
                    continue
                parts = line.strip().split("|")
                if len(parts) != 4:
                    continue

                entered_date, description, category, amount_text = parts
                try:
                    amount = float(amount_text)
                except ValueError:
                    continue

                if not math.isfinite(amount) or amount <= 0:
                    continue

                expenses.append({
                    "date": entered_date,
                    "description": description,
                    "category": category.strip().title(),
                    "amount": amount,
                })
    except FileNotFoundError:
        expenses = []
    return expenses


def save_expenses(expenses):
    with open(data_file, "w", encoding="utf-8") as file:
        for expense in expenses:
            file.write(
            f"{expense['date']}|{expense['description']}|{expense['category']}|{expense['amount']}\n"
            )


expenses = read_expenses()

while True:
    print("\n===== Expense Tracker =====")
    print('''   1. Add expense
   2. View expenses
   3. Total spent
   4. Category summary
   5. Edit expense
   6. Delete expense
   7. Exit''')
    choice = input("Choose an option: ")

    if choice == "1":
        description = input("What did you spend money on? ").strip()
        if description == "" or not any(letter.isalpha() for letter in description):
            print("Please enter a description using words, like Lunch or Bus fare.")
            continue

        category = input("Category (for example, Food or Transport): ").strip().title()
        if category == "" or not any(letter.isalpha() for letter in category):
            print("Please enter a category using words, like Food or Transport.")
            continue

        try:
            amount = float(input("How much did you spend? "))
            if not math.isfinite(amount) or amount <= 0:
                print("Enter a valid, finite amount greater than 0.")
                continue
        except ValueError:
            print("Please enter a number, like 12.50.")
            continue

        expense = {
            "date": date.today().strftime("%Y-%m-%d"),
            "description": description,
            "category": category,
            "amount": amount,
        }
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added.")

    elif choice == "2":
        if len(expenses) == 0:
            print("You have not added any expenses yet.")
        else:
            print("\nYour expenses:")
            for expense in expenses:
                print(
                    expense["date"],
                    "-",
                    expense["description"],
                    "(" + expense["category"] + ")",
                    "- Rs.",
                    format(expense["amount"], ".2f"),
                )

    elif choice == "3":
        total = 0
        for expense in expenses:
            total = total + expense["amount"]

        print("Total spent: Rs.", format(total, ".2f"))

    elif choice == "4":
        if len(expenses) == 0:
            print("You have not added any expenses yet.")
        else:
            category_totals = {}
            for expense in expenses:
                category = expense["category"]
                if category in category_totals:
                    category_totals[category] = category_totals[category] + expense["amount"]
                else:
                    category_totals[category] = expense["amount"]

            print("\nSpending by category:")
            for category in category_totals:
                print(category, "- Rs.", format(category_totals[category], ".2f"))

    elif choice == "5":
        if len(expenses) == 0:
            print("You have not added any expenses yet.")
            continue

        for number, expense in enumerate(expenses, start=1):
            print(number, "-", expense["date"], "-", expense["description"],
                  "(" + expense["category"] + ")", "- Rs.", format(expense["amount"], ".2f"))

        try:
            number = int(input("Which expense number do you want to edit? "))
        except ValueError:
            print("Please enter a number.")
            continue

        if number < 1 or number > len(expenses):
            print("That number is not in the list.")
            continue

        expense = expenses[number - 1]

        new_description = input(f"Description [{expense['description']}]: ").strip()
        new_category = input(f"Category [{expense['category']}]: ").strip().title()
        new_amount_text = input(f"Amount [{expense['amount']}]: ").strip()

        # Check the amount first, so nothing changes if it is invalid
        new_amount = expense["amount"]
        if new_amount_text != "":
            try:
                new_amount = float(new_amount_text)
            except ValueError:
                print("Please enter a number, like 12.50.")
                continue
            if not math.isfinite(new_amount) or new_amount <= 0:
                print("Enter a valid, finite amount greater than 0.")
                continue

        if new_description != "":
            expense["description"] = new_description
        if new_category != "":
            expense["category"] = new_category
        expense["amount"] = new_amount

        save_expenses(expenses)
        print("Expense updated.")


    elif choice == "6":
        if len(expenses) == 0:
            print("You have not added any expenses yet.")
            continue

        for number, expense in enumerate(expenses, start=1):
            print(number, "-", expense["date"], "-", expense["description"],
                  "(" + expense["category"] + ")", "- Rs.", format(expense["amount"], ".2f"))

        try:
            number = int(input("Which expense number do you want to delete? "))
        except ValueError:
            print("Please enter a number.")
            continue

        if number < 1 or number > len(expenses):
            print("That number is not in the list.")
            continue

        removed = expenses.pop(number - 1)
        save_expenses(expenses)
        print("Deleted:", removed["description"])

    else:
        print("Please choose a number from 1 to 6.")
