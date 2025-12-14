import json
from datetime import datetime

FILENAME = "expence.json"


# Load Expense
def load_expense():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expense(expense):
    with open(FILENAME, "w") as file:
        json.dump(expense, file, indent=4)


# VALIDATION FUNCTION

# Amount validation
def validate_amount():
    while True:
        amt_in = input("Enter amount: ").strip()
        if amt_in.lower() == "cancel":
            print("Cancelled.")
            return None
        try:
            amount = float(amt_in)
            if amount > 0:
                return amount
            print("Amount must be greater than 0.")
        except:
            print("Invalid number.")


# Category Validation
def validate_category():
    categories = ["Food", "Transport", "Shopping", "Other"]
    while True:
        category = input("Enter category (Food/Transport/Shopping/Other): ").strip()
        if category.lower() == "cancel":
            print("Cancelled.")
            return None
        if category in categories:
            return category
        print("Invalid category.")


# Description Validation
def validate_description():
    while True:
        desc = input("Enter description: ").strip()
        if desc.lower() == "cancel":
            print("Cancelled.")
            return None
        if desc != "":
            return desc
        print("Description cannot be empty.")


# Date Validation
def validate_date():
    while True:
        date_in = input("Enter date (DD-MM-YYYY): ").strip()
        if date_in.lower() == "cancel":
            print("Cancelled.")
            return None
        if date_in == "":
            return datetime.now().strftime("%d-%m-%Y")
        try:
            datetime.strptime(date_in, "%d-%m-%Y")
            return date_in
        except:
            print("Invalid date format.")


# Expense Manager Function

# Add Expense
def add_expense(expense):
    amount = validate_amount()
    if amount is None:
        return

    category = validate_category()
    if category is None:
        return

    description = validate_description()
    if description is None:
        return

    date = validate_date()
    if date is None:
        return

    new_expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expense.append(new_expense)
    save_expense(expense)
    print("Expense added successfully!")


# View all Expense
def view_all_expense(expense):
    if not expense:
        print("No expenses found.")
        return

    print("All Expense")
    for i, exp in enumerate(expense, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | {exp['amount']} | {exp['description']}")


# View Expense by Category
def view_by_category(expense):
    category = input("Enter category: ").strip()

    print("Expense by Category")
    found = False

    for exp in expense:
        if exp["category"].lower() == category.lower():
            print(f"{exp['date']} | {exp['category']} | {exp['amount']} | {exp['description']}")
            found = True

    if not found:
        print("No expenses in this category.")


# Edit Expense
def edit_expense(expense):
    if not expense:
        print("No expenses to edit.")
        return

    view_all_expense(expense)

    try:
        index = int(input("Enter expense number to edit: ")) - 1
        if index < 0 or index >= len(expense):
            print("Invalid number.")
            return
    except ValueError:
        print("Invalid input.")
        return

    exp = expense[index]

    print("To keep old value leave blank")

    new_amt = input(f"Amount ({exp['amount']}): ").strip()
    if new_amt:
        try:
            val = float(new_amt)
            if val > 0:
                exp["amount"] = val
        except:
            print("Invalid amount.")

    new_cat = input(f"Category ({exp['category']}): ").strip()
    if new_cat:
        exp["category"] = new_cat

    new_desc = input(f"Description ({exp['description']}): ").strip()
    if new_desc:
        exp["description"] = new_desc

    new_date = input(f"Date ({exp['date']}): ").strip()
    if new_date:
        try:
            datetime.strptime(new_date, "%d-%m-%Y")
            exp["date"] = new_date
        except:
            print("Invalid date.")

    save_expense(expense)
    print("Expense updated!")


# Delete Expense
def delete_expense(expense):
    if not expense:
        print("No expenses to delete.")
        return

    view_all_expense(expense)

    try:
        index = int(input("Enter expense number to delete: ")) - 1
        if index < 0 or index >= len(expense):
            print("Invalid number.")
            return
    except ValueError:
        print("Invalid input.")
        return

    confirm = input("Are you sure? (yes/no): ").lower()
    if confirm == "yes":
        expense.pop(index)
        save_expense(expense)
        print("Expense deleted.")
    else:
        print("Delete cancelled.")


# Monthly Summary
def monthly_summary(expense):
    if not expense:
        print("No expenses available.")
        return

    monthly_totals = {}
    category_totals = {}

    for exp in expense:
        month = exp["date"][3:]
        monthly_totals[month] = monthly_totals.get(month, 0) + exp["amount"]
        category_totals[exp["category"]] = category_totals.get(exp["category"], 0) + exp["amount"]

    print("Monthly Summary")
    for m, t in monthly_totals.items():
        print(f"{m}: {t}")

    top_category = max(category_totals, key=category_totals.get)
    print(f"Highest Spending Category: {top_category} -> {category_totals[top_category]}")


# Main code
def main():
    expense = load_expense()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Edit Expense")
        print("5. Delete Expense")
        print("6. Monthly Summary")
        print("7. Exit")

        choice = input("Choose option (1-7): ").strip()

        if choice == "1":
            add_expense(expense)
        elif choice == "2":
            view_all_expense(expense)
        elif choice == "3":
            view_by_category(expense)
        elif choice == "4":
            edit_expense(expense)
        elif choice == "5":
            delete_expense(expense)
        elif choice == "6":
            monthly_summary(expense)
        elif choice == "7":
            print("Thank you for using Expense Tracker")
            break
        else:
            print("Invalid option. Enter 1–7.")


if __name__ == "__main__":
    main()
