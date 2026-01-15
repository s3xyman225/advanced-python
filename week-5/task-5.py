class BankAccount:
    def __init__(self, owner, balance):   
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit must be positive")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough money")

    def get_balance(self):
        return self.__balance


account = BankAccount("Nazar", 1500)   
account.deposit(400)
account.withdraw(2000)

print(account.get_balance())
