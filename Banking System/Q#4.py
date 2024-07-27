class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def account_detail(self):
        print(f"""Account Number: {self.account_number}
                  Account Holder Name: {self.account_holder}
                  Balance : {self.balance}""")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs.{amount} in your account successfully..")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn Rs.{amount} from your account")
        else:
            print("Insufficient fund..")

    def check_balance(self):
        print(f"Current available balance in your account is {self.balance}")

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = []

    def open_account(self, account_number, balance=0):
        account = BankAccount(account_number, self.name, balance)
        self.accounts.append(account)
        print(f"Account has been successfully open with Account number: {account_number} and Initial Balance: {balance}")
        return account

    def close_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
        print("Account not found")

class Bank:
    customers = []
    accounts = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"{customer.name} added successfully")

    def transfer_fund(self, sender_account, receiver_account, amount):
        if sender_account.balance >= amount:
            sender_account.withdraw(amount)
            receiver_account.deposit(amount)
        else:
            print("Insufficient fund")

    def get_account_detail(self, account_number):
        for customer in self.customers:
            for account in customer.accounts:
                if account.account_number == account_number:

                 return account


bank = Bank()
customer1 = Customer("hussain", "CID-12")
customer2 = Customer("Asif","CID-34")
bank.add_customer(customer1)
bank.add_customer(customer2)

customer1.open_account(123,100)
customer2.open_account(456,500)

a = customer1.open_account(123,100)
b = customer2.open_account(456,500)
bank.transfer_fund(a,b,50)
a.check_balance()
b.check_balance()
bank.get_account_detail(123)
