class Bank_Account:
    def __init__(self):
        self.balance = 500
        print("Welcome to people N Tech Bank")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited BDT: "))
        self.balance += amount
        print("Amount Deposited BDT:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn BDT: "))
        if self.balance >= amount:
            self.balance -= amount
            print("You have Withdrawn BDT:", amount)
        else:
            print("Insufficient balance  ")

    def display(self):
        print("Net Available Balance BDT=", self.balance)

s = Bank_Account()

s.display()
s.deposit()
s.deposit()
s.withdraw()
s.deposit()
s.withdraw()
s.withdraw()
s.display()


