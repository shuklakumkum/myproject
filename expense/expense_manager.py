from validator import (
    validate_amount,
    validate_category,
    validate_description,
    validate_date,
)
from file_handler import save_expense
from datetime import datetime


# Add a new expense
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

    expense.append({
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    })

    save_expense(expense)
    print("Expense added successfully!")


# Display all expenses
def view_all_expense(expense):
    if not expense:
        print("No expenses found.")
        return

    print("\n=== All Expenses ===")
    for i, exp in enumerate(expense, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | {exp['amount']} | {exp['description']}")


# Edit an existing expense
def edit_expense(expense):
    if not expense:
        print("No expenses to edit.")
        return

    view_all_expense(expense)

    try:
        index = int(input("Enter expense number to edit: ")) - 1
        if index < 0 or index >= len(expense):
            print("Expense does not exist.")
            return
    except ValueError:
        print("Invalid input.")
        return

    exp = expense[index]

    # Update if user enter new values
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
    print("Expense updated successfully!")


# Delete expense
def delete_expense(expense):
    if not expense:
        print("No expenses to delete.")
        return

    view_all_expense(expense)

    try:
        index = int(input("Enter expense number to delete: ")) - 1
        if index < 0 or index >= len(expense):
            print("Expense does not exist.")
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


# Monthly summary 
def monthly_summary(expense):
    if not expense:
        print("No expenses available.")
        return

    monthly = {}
    category = {}

    for exp in expense:
        month = exp["date"][3:]
        monthly[month] = monthly.get(month, 0) + exp["amount"]
        category[exp["category"]] = category.get(exp["category"], 0) + exp["amount"]

    print("Monthly Summary")
    for m, t in monthly.items():
        print(f"{m}: {t}")

    top = max(category, key=category.get)
    print(f"Highest Spending Category: {top} -> {category[top]}")
