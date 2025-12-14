import json

# File name 
FILENAME = "expence.json"


# Load expense
def load_expense():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return empty list if file not found or corrupted
        return []


# Save expense
def save_expense(expense):
    with open(FILENAME, "w") as file:
        json.dump(expense, file, indent=4)
