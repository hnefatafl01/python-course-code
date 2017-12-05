class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self,amount):
        self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(self.balance )

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

class Checking(Account):
    def __init__(self,filepath, fee):
        self.fee = fee
        Account.__init__(self, filepath)

account = Account("./balance.txt")
checking = Checking("./balance.txt", 1)
# account.deposit(200)
# print(account.balance)
# account.withdraw(100)
# print(account.balance)
print(checking.balance)
checking.transfer(20)
checking.deposit(110)
print(checking.balance)
