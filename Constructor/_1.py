class BankAccount:
    def __init__(self,account_no,holder_name,starting_balance):
        self.account_no=account_no
        self.holder_name=holder_name
        self.starting_balance=starting_balance

    def display(self):
        print(f"Account number is :{self.account_no}")
        print(f"Account holder name is :{self.holder_name}")
        print(f"Account starting balance is :{self.starting_balance}")


obj=BankAccount(718236481,"Kamran",56000)
obj.display()