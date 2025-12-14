from file_handler import load_expense
from expense_manager import (
    add_expense,
    view_all_expense,
    edit_expense,
    delete_expense,
    monthly_summary,
)


# Main program 
def main():
    expense = load_expense()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Monthly Summary")
        print("6. Exit")

        choice = input("Choose option (1-6): ")

        if choice == "1":
            add_expense(expense)
        elif choice == "2":
            view_all_expense(expense)
        elif choice == "3":
            edit_expense(expense)
        elif choice == "4":
            delete_expense(expense)
        elif choice == "5":
            monthly_summary(expense)
        elif choice == "6":
            print("Thank you for using Expense Tracker")
            break
        else:
            print("Invalid option.")


# Program entry point
if __name__ == "__main__":
    main()
