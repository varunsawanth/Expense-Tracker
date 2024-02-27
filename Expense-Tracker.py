import csv
import os

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = set()

    def add_expense(self, amount, category):
        self.expenses.append({"amount": amount, "category": category})
        self.categories.add(category)

    def save_expenses(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["amount", "category"])
            writer.writeheader()
            writer.writerows(self.expenses)

    def load_expenses(self, filename):
        if os.path.exists(filename):
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.expenses.append({"amount": float(row["amount"]), "category": row["category"]})
                    self.categories.add(row["category"])

    def view_expenses(self):
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        print("Total Expenses: $", total_expenses)
        print("Categories:")
        for category in self.categories:
            category_expenses = sum(expense["amount"] for expense in self.expenses if expense["category"] == category)
            print(f"{category}: ${category_expenses}")

def main():
    expense_tracker = ExpenseTracker()
    expense_tracker.load_expenses("expenses.csv")

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            expense_tracker.add_expense(amount, category)
        elif choice == "2":
            expense_tracker.view_expenses()
        elif choice == "3":
            expense_tracker.save_expenses("expenses.csv")
            print("Expenses saved successfully. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
