class SavingsAccount:
    def __init__(self, name, initial_balance, pin_number):
        self.name = name
        self.balance = initial_balance
        self.pin_number = pin_number

    def display_account_info(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")
        print(f"PIN: {self.pin_number}")


class BusinessAccount:
    def __init__(self, business_name, initial_balance):
        self.business_name = business_name
        self.balance = initial_balance

    def display_account_info(self):
        print(f"Business Name: {self.business_name}")
        print(f"Balance: {self.balance}")



savings = SavingsAccount("kl", 1500, 1234)
business = BusinessAccount("bcci", 5000)


savings.display_account_info()

business.display_account_info()


class SavingsAccount:
    def __init__(self, name, initial_balance, pin_number):
        self.name = name
        self.balance = initial_balance
        self.pin_number = pin_number
        self.is_active = True
        self.atm_requested = False
        self.cheque_book_requested = False
        self.daily_withdrawal_limit = 1000  

    def check_balance(self, entered_pin):
        if entered_pin != self.pin_number:
            print(" Error: Invalid PIN.")
        elif not self.is_active:
            print("Account is frozen. Cannot check balance.")
        else:
            print(f" Account Active. Current Balance: {self.balance}")

   
    def withdraw(self, entered_pin, amount):
        if entered_pin != self.pin_number:
            print("Error: Invalid PIN.")
        elif not self.is_active:
            print("Account is frozen. Cannot withdraw funds.")
        elif amount > self.balance:
            print("Error: Insufficient balance.")
        elif amount > self.daily_withdrawal_limit:
            print(f" Error: Amount exceeds daily withdrawal limit ({self.daily_withdrawal_limit}).")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New Balance: {self.balance}")

   
    def deposit(self, entered_pin, amount):
        if entered_pin != self.pin_number:
            print("Error: Invalid PIN.")
        elif amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f" Deposit successful. New Balance: {self.balance}")

    def request_atm_card(self):
        if self.atm_requested:
            print("ATM card already requested.")
        else:
            self.atm_requested = True
            print(" ATM card request approved.")

    def request_cheque_book(self):
        if self.cheque_book_requested:
            print("Cheque book already requested.")
        else:
            self.cheque_book_requested = True
            print("Cheque book request approved.")
    def freeze_account(self):
        if self.freeze_account:
            print("your account will already freeze")
        else:
            self.freeze_account= False
            print("your account frozen")
    def unfreeze_account(self):
        if self.unfreeze_account:
            print("your account is activeted ")
        else:
            self.unfreeze_account=True
            print("your account is unfrozeen")



savings= SavingsAccount("fire",9000,222)



savings.withdraw(222,150)
savings.deposit(222,120)
savings.request_atm_card()
savings.request_atm_card()
savings.request_cheque_book()
savings.freeze_account()
savings.unfreeze_account()

class BusinessAccount:
    def __init__(self, business_name, initial_balance,enter_pin):
        self.business_name = business_name
        self.balance = initial_balance
        self.pin=enter_pin

