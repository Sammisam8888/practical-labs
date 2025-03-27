class Bank:
    def __init__(self, accno, accbal):
        self.accno = accno
        self.accbal = accbal

    def deposit(self, amt):
        self.accbal += amt

    def withdraw(self, amt):
        if self.accbal < amt:
            print("Insufficient balance, cannot withdraw amount")
            return False
        else:
            self.accbal -= amt
        return True

acc1 = Bank("123456", 1000)
acc2 = Bank("654321", 2000)

acc1.deposit(500)
print(f"Account {acc1.accno} balance after deposit: {acc1.accbal}")

acc2.withdraw(3000)
print(f"Account {acc2.accno} balance : {acc2.accbal}")
