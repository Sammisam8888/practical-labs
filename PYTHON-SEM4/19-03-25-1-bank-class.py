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

if acc2.withdraw(1500):
    print(f"Account {acc2.accno} balance after withdrawal: {acc2.accbal}")
else:
    print(f"Account {acc2.accno} withdrawal failed. Current balance: {acc2.accbal}")
