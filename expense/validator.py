from datetime import datetime


# Validate expense 
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


# Validate category 
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


# Validate description
def validate_description():
    while True:
        desc = input("Enter description: ").strip()

        if desc.lower() == "cancel":
            print("Cancelled.")
            return None

        if desc:
            return desc

        print("Description cannot be empty.")


# Validate date input
def validate_date():
    while True:
        date_in = input("Enter date (DD-MM-YYYY): ").strip()

        if date_in.lower() == "cancel":
            print("Cancelled.")
            return None

        # Use today date if empty
        if date_in == "":
            return datetime.now().strftime("%d-%m-%Y")

        try:
            datetime.strptime(date_in, "%d-%m-%Y")
            return date_in
        except:
            print("Invalid date format.")
