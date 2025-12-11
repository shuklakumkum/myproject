import json
import sys
from datetime import datetime

FILENAME = "expence.json"

#Load all expense from the json file

def load_expense():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

#Save the expense
def save_expense(expense):
    with open(FILENAME, "w") as file:
        json.dump(expense, file, indent=4)

#Add a new expense

def add_expense(expense):
    
    #Amount validation
    
    while True:
        amt_in = input("Enter amount: ").strip()
        if amt_in.lower() == "cancel":
            print("Add cancelled  Returning to menu.")
            return
        try:
            amount = float(amt_in)
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid amount please Enter a numeric value.")

    #Category validation
            
    valid_categories = ["Food", "Transport", "Shopping", "Other"]
    while True:
        category = input("Enter category (Food/Transport/Shopping/Other) : ").strip()
        if category.lower() == "cancel":
            print("Add cancelled. Returning to menu.")
            return
        if category in valid_categories:
            break
        print(f"Invalid category please Choose one of: {', '.join(valid_categories)}")

    #Description validation
        
    while True:
        description = input("Enter description: ").strip()
        if description.lower() == "cancel":
            print("Add cancelled.Returning to menu.")
            return
        if description == "":
            print("Description cannot be empty. Try again.")
            continue
        break

    #Date validation
    
    while True:
        date_input = input("Enter date (DD-MM-YYYY): ").strip()
        if date_input.lower() == "cancel":
            print("Add cancelled. Returning to menu.")
            return
        if date_input == "":
            date = datetime.now().strftime("%d-%m-%Y")
            break
        try:
            datetime.strptime(date_input, "%d-%m-%Y")
            date = date_input
            break
        except ValueError:
            print("Invalid date format please Use DD-MM-YYYY ")

    new_expense = {
        "amount": amount,
        "description": description,
        "category": category,
        "date": date
    }

    expense.append(new_expense)
    save_expense(expense)
    print("Expense added successfully!")

#View all expenses

def view_all_expense(expense):
    if not expense:
        print("No expense found.")
        return

    print("All Expenses")
    print("Date | Category | Amount | Description")
    for exp in expense:
        print(f"{exp['date']} | {exp['category']} | {exp['amount']} | {exp['description']}")

#View expenses based on selected category

def view_by_category(expense):
    valid_categories = ["Food", "Transport", "Shopping", "Other"]
    category = input("Enter category (Food/Transport/Shopping/Other): ").strip()

    print("Expenses By Category")
    print("Date | Category | Amount | Description")

    found = False
    for exp in expense:
        if exp["category"].lower() == category.lower():
            print(f"{exp['date']} | {exp['category']} | {exp['amount']} | {exp['description']}")
            found = True

    if not found:
        print("No expense in this category.")

#Show total spending amount

def show_total(expense):
    total = sum(exp["amount"] for exp in expense)
    print(f"Total spending: {total}")

#Main code

def main():
    expense = load_expense()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Show Total Spending")
        print("5. Exit")

        choice = input("Choose option (1-5): ").strip()

        if choice == "1":
            try:
                add_expense(expense)
            except Exception as e:
                print("An unexpected error occurred while adding expense:", str(e))

        elif choice == "2":
            view_all_expense(expense)

        elif choice == "3":
            view_by_category(expense)

        elif choice == "4":
            show_total(expense)

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            sys.exit(0) 

        else:
            print("Invalid option please Enter between 1 and 5.")

#Program entry point

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)
