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

class money_in(transactions): 
    def __init__ (self, transaction_id, amount, date, source): 
        super().__init__(transaction_id, amount, date, ) 
        self.source = source

class money_out(transactions): 
    def __init__ (self, transaction_id, amount, date, type): 
        super().__init__(transaction_id, amount, date, ) 
        self.type = type

money1 = money_in("paycheck", 1500, "8/12/2026", "Job")
money2 = money_in("newyear money", 100, "1/1/2026", "Gift")
money3 = money_out("shopping", 80, "8/10/2026", "clothes")
money4 = money_out("grocery shopping", 150, "8/11/2026", "food")

money_list = [money1, money2, money3, money4]

for money in money_list:
    print(f"Transaction ID: {money.transaction_id}, Amount: {money.amount}, Date: {money.date}, Description: {getattr(money, 'source', getattr(money, 'type', ''))}")
    print(f"Good Price: {money.good_price()}")
    