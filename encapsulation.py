class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private variable using "__" 
        self.__balance = balance                # private variable

    # Getter for balance
    def get_balance(self):   #getter method
        return self.__balance

    # Setter for balance (with validation)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount!")


account = BankAccount("12345", 1000)

# Direct access is restricted
# print(account.__balance)   #This will raise an AttributeError

# Access via methods
print("Initial Balance:", account.get_balance())  # Output: 1000

account.deposit(500)
print("Balance after deposit:", account.get_balance())  #Output: 1500

account.withdraw(200)
print("Balance after withdrawal:", account.get_balance())  # Output: 1300

account.withdraw(2000)  #Insufficient balance
