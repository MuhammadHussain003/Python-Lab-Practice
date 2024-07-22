class BankAccount:
    def __init__(self,__account_num,__holder_name,__balance):
        self.__account_num = __account_num
        self.__holder_name = __holder_name
        self.__balance = __balance

    def display(self):
        print(f"""
                   Account number : {self.__account_num}
                   Account holder name : {self.__holder_name}
                   Available amount : {self.__balance}
                   """)

    def depositing(self,amount):
        self.__balance+=amount
        print(f"Your have successfully deposit Rs:{amount} in your account")

    def withdraw(self,amount):
        self.__balance-=amount
        print(f"you have successfully withdraw Rs:{amount} from your account ")

    def checking_balance(self):
        print("Current amount is Rs:",self.__balance)


b=BankAccount(23981723,"asif",30000)
b.display()
b.depositing(5000)
b.checking_balance()
b.withdraw(15000)
b.checking_balance()

