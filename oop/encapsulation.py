class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance #atributo privado
        
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
        else:
            print("Insufficiente funds")
            
    def getBalance(self):
        return self.__balance

#Uso de encapsulamiento
account = BankAccount("Dereck", 1000)
account.deposit(500)
account.withdraw(300)
print("Final Balance:", account.getBalance())