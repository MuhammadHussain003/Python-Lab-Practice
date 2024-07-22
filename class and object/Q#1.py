class BankAccount:

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    def owner_account(self):
        print("Account number is:",self.account_number)
        print("Account holder name is ",self.holder_name)
        print("Available balance is Rs:",self.balance)
    def deposit(self, amount):
        self.balance+=amount
        print(f"Successfully deposit Rs:{amount} in your account..")

    def withdraw(self, amount):
        if self.balance>amount:
          self.balance-=amount
          print(f"You have successfully withdraw Rs:{amount} from your account..")
        else:
          print("You entered invalid amount......")

    def checking_balance(self,amount):
        if amount>0:
            print(f"Available amount is Rs:{amount}")
        else:
            print("Insufficient Balance...")

obj=BankAccount("1235123","Asif Ali",60000)
obj.owner_account()
obj.deposit(4000)
obj.owner_account()
obj.withdraw(40000)
obj.owner_account()