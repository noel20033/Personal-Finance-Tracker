class BudgetApp:
    def __init__(self):
        self.income = 0
        self.expenses = []
        self.categories = {}

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
