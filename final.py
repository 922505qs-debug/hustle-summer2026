class transactions: 
    def __init__(self, transaction_id, amount, date, description): 
        self.transaction_id = transaction_id 
        self.amount = amount 
        self.date = date 
        self.description = description
    def good_price(self): 
        if self.amount < 0: 
            return False 
        else: 
            return True

class income(transactions): 
    def __init__ (self, name, amount, date, source): 
        super().__init__(name, amount, date, source) 
        self.source = source
    def show_info(self): 
        return f"Transaction ID: {self.transaction_id}, Amount: {self.amount}, Date: {self.date}, Source: {self.source}"

class expense(transactions): 
    def __init__ (self, name, amount, date, category): 
        super().__init__(name, amount, date, category) 
        self.category = category
    def show_info(self): 
        return f"Transaction ID: {self.transaction_id}, Amount: {self.amount}, Date: {self.date}, Category: {self.category}"


money_list = []

for money in money_list:
    print(money.show_info())
    print(f"Good Price: {money.good_price()}")
    
class money_tracking:
    def __init__(self):
        self.money_list = []

    def add_income(self, income):
        name = input("What is the income name?")
        amount = float(input("What is the income amount?"))
        date = input("What day was the income recieved?")
        source = input("What is the source of the income?")
        income = income(name, amount, date, source)

        if income.good_price():
            self.money_list.append(income)
            print("Income added successfully.")
            print()
        else: 
            print("Invalid income amount. Income not added.")
            print()
    
    def add_expense(self, expense):
        name = input("What is the expense name?")
        amount = float(input("What is the expense amount?"))
        date = input("What day was the expense made?")
        category = input("What is the category of the expense?")
        expense = expense(name, amount, date, category)

        if expense.good_price():
            self.money_list.append(expense)
            print("Expense added successfully.")
            print()
        else: 
            print("Invalid expense amount. Expense not added.")
            print()

    def show_all_transactions(self):
        for money in self.money_list:
            print(money.show_info())
            print(f"Good Price: {money.good_price()}")
        if len(self.money_list) == 0:
            print("No transactions to show.")
        else: 
            print(f"--- All Transactions ---")
            print(f"Total transactions: {len(self.money_list)}")
            for money in self.money_list:
                money.show_info()

    def total_income(self):
        total = 0
        for money in self.money_list:
            if isinstance(money, income):
                total += money.amount
        return total

    def total_expense(self):
        total = 0
        for money in self.money_list:
            if isinstance(money, expense):
                total += money.amount
        return total
    def show_balance(self):
       income = self.total_income()
       expense = self.total_expense()
       balance = income - expense
       print(" --- Money Income and Expense Tracker ---")
       print(f"Total Income: ${income}")
       print(f"Total Expense: ${expense}")
       print(f"Balance: ${balance}")
       print()
    def start(self):
        while True:
            print ("--- Money Income and Expense Tracker ---")
            print("Please select an option:")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. Show All Transactions")
            print("4. Show Balance")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_income(income)
            elif choice == "2":
                self.add_expense(expense)
            elif choice == "3":
                self.show_all_transactions()
            elif choice == "4":
                self.show_balance()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

tracker = money_tracking()
tracker.start()