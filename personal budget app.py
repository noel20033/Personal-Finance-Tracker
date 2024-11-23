import openpyxl
from openpyxl import Workbook

class BudgetApp:
    def __init__(self):
        self.income = 0
        self.expenses = []
        self.categories = {}
        self.file_name = "budget.xlsx"

    def add_income(self, amount):
        self.income += amount
        print(f"Added income: ${amount:.2f}. Total income: ${self.income:.2f}.")

    def add_expense(self, category, amount):
        if amount > self.income - self.total_expenses():
            print("Not enough funds for this expense.")
            return
        self.expenses.append((category, amount))
        if category in self.categories:
            self.categories[category] += amount
        else:
            self.categories[category] = amount
        print(f"Added expense: ${amount:.2f} to category '{category}'.")

    def total_expenses(self):
        return sum(amount for _, amount in self.expenses)

    def get_balance(self):
        return self.income - self.total_expenses()

    def display_summary(self):
        print("\n--- Budget Summary ---")
        print(f"Total Income: ${self.income:.2f}")
        print(f"Total Expenses: ${self.total_expenses():.2f}")
        print(f"Balance: ${self.get_balance():.2f}\n")
        print("Expenses by Category:")
        for category, amount in self.categories.items():
            print(f"  {category}: ${amount:.2f}")
        print("----------------------")

    def save_to_excel(self):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Budget Summary"

        # Add headers
        sheet.append(["Income", self.income])
        sheet.append([""])
        sheet.append(["Category", "Amount"])

        # Add expenses
        for category, amount in self.categories.items():
            sheet.append([category, amount])

        # Add summary
        sheet.append([""])
        sheet.append(["Total Expenses", self.total_expenses()])
        sheet.append(["Balance", self.get_balance()])

        # Save to file
        workbook.save(self.file_name)
        print(f"Budget data saved to '{self.file_name}'.")

def main():
    app = BudgetApp()
    while True:
        print("\n--- Budget App ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Save to Excel")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            try:
                amount = float(input("Enter income amount: $"))
                app.add_income(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "2":
            category = input("Enter expense category: ")
            try:
                amount = float(input("Enter expense amount: $"))
                app.add_expense(category, amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "3":
            app.display_summary()
        elif choice == "4":
            app.save_to_excel()
        elif choice == "5":
            print("Exiting the Budget App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
