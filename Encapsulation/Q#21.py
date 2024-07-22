class BankAccount:
    def __init__(self,account_number,holder_name,balance):
        self.__account_number=account_number
        self.__holder_name=holder_name
        self.__balance=balance
    def Display(self):
        print(f"""
              Account Number is : {self.__account_number}
              Account holder name : {self.__holder_name}
              Available balance is : {self.__balance}
""")

    def Deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Successfully deposit Rs:{amount} in your account")
        else:
            print("Invalid amount..")
    def withdraw(self,amount):
        if amount>0:
            self.__balance-=amount
            print(f"""
            Account No. {self.__account_number}
            DEBIT with amount Rs.{amount} successfully""")
        else:
            print("Invalid amount")
    def check(self):
        print(f"Available amount Rs.{self.__balance}")




b = BankAccount(5324321,"Muhammad Zubair",23000)
b.Display()
b.check()
b.withdraw(2000)
b.Display()