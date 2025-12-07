import json
from datetime import datetime

FILENAME = "expenses.py"

# Load expenses from file
def load_expenses():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add new expense
def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount!")
        return

    category = input("Enter category (Food/Transport/Shopping/Other): ")
    description = input("Enter description: ")

    date_input = input("Date (DD-MM-YYYY) or press Enter for today: ")
    if date_input.strip() == "":
        date = datetime.now().strftime("%d-%m-%Y")
    else:
        date = date_input

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")

# View all expenses
def view_all_expenses(expenses):
    if not expenses:
        print("⚠️ No expenses found.")
        return

    print("\n--- All Expenses ---")
    print("Date        | Category  | Amount | Description")
    print("-" * 50)

    for exp in expenses:
        print(f"{exp['date']} | {exp['category']:<9} | {exp['amount']:<6} | {exp['description']}")

# View expenses by category
def view_by_category(expenses):
    category = input("Enter category name: ")

    found = False
    print("\n--- Expenses By Category ---")
    print("Date        | Category  | Amount | Description")
    print("-" * 50)

    for exp in expenses:
        if exp["category"].lower() == category.lower():
            print(f"{exp['date']} | {exp['category']:<9} | {exp['amount']:<6} | {exp['description']}")
            found = True

    if not found:
        print("⚠️ No expenses found in this category.")

# Show total spending
def show_total(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Spending: ₹{total}")

# Main Menu
def main():
    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Show Total Spending")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_all_expenses(expenses)

        elif choice == "3":
            view_by_category(expenses)

        elif choice == "4":
            show_total(expenses)

        elif choice == "5":
            print("👋 Thank you for using Expense Tracker!")
            break

        else:
            print("❌ Invalid choice!")

# Run Program
main()
