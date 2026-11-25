
import csv
from datetime import datetime

expenses = []

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date! Please use YYYY-MM-DD.")
        return

    category = input("Enter expense category: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Invalid amount!")
        return

    expense = {
        "date": date,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")


def show_totals():
    totals = {}

    for expense in expenses:
        category = expense["category"]

        if category in totals:
            totals[category] += expense["amount"]
        else:
            totals[category] = expense["amount"]

    print("\n--- Category-wise Spending ---")

    for category, total in totals.items():
        print(category, ":", round(total, 2))


def save_expenses():
    with open("expenses.csv", "w", newline="") as file:
        fields = ["date", "category", "amount"]

        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        writer.writerows(expenses)

    print("\nExpenses saved to expenses.csv")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. Show Category Totals")
    print("3. Save Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_totals()

    elif choice == "3":
        save_expenses()

    elif choice == "4":
        save_expenses()
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Try again.")
