
from tabulate import tabulate
import sys


class ATM:
    def __init__(self):
        self.initial_balance = 100000
        self.balance = self.initial_balance
        self.transaction_history = []

    
    def deposit(self, amount):
        self.balance += amount
        transaction_detail = f'Deposited Rs.{amount}'
        self.transaction_history.append(transaction_detail)
        return f'Deposited Rs.{amount}. New balance: Rs.{self.balance}'

    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Withdrawn Rs.{amount}')
            return f'Withdrawn Rs.{amount}. New balance: Rs.{self.balance}'
        else:
            return 'Insufficient funds'


    def transfer(self, amount, recipient, transfer_type):
        if amount <= self.balance:
            self.balance -= amount
            if transfer_type == 1:
                transaction_detail = f'Transferred Rs.{amount} to {recipient}'
                self.transaction_history.append(transaction_detail)
            elif transfer_type == 2:
                transaction_detail = f'Transferred Rs.{amount} to {recipient}'
                self.transaction_history.append(transaction_detail)
            elif transfer_type == 3:
                transaction_detail = f'Transferred Rs.{amount} to {recipient}'
                self.transaction_history.append(transaction_detail)
            return f'Transferred Rs.{amount} to {recipient}. New balance: Rs.{self.balance}'
        else:
            return 'Insufficient funds'

    
    def get_balance(self):
        return f'Current balance: Rs.{self.balance}'

   
    def get_transaction_history(self):
        return self.transaction_history
    

    
def display_logo():
    
    welcome_logo = """


 █     █▓█████ ██▓    ▄████▄  ▒█████  ███▄ ▄███▓█████     ▐██▌    
▓█░ █ ░█▓█   ▀▓██▒   ▒██▀ ▀█ ▒██▒  ██▓██▒▀█▀ ██▓█   ▀     ▐██▌    
▒█░ █ ░█▒███  ▒██░   ▒▓█    ▄▒██░  ██▓██    ▓██▒███       ▐██▌    
░█░ █ ░█▒▓█  ▄▒██░   ▒▓▓▄ ▄██▒██   ██▒██    ▒██▒▓█  ▄     ▓██▒    
░░██▒██▓░▒████░██████▒ ▓███▀ ░ ████▓▒▒██▒   ░██░▒████▒    ▒▄▄     
                                         
                                                                                                            
    """


    print(welcome_logo)



def atm_interface():

    
    atm = ATM()

    
    display_logo() 
    print("Welcome to the ATM Interface")

   
    user_id = input("Enter User ID: ")
    pin = input("Enter PIN: ")

   
    if user_id == "ABC" and pin == "12345":
        print("Login successful!\n")

        while True:
            print("ATM Operations:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Quit")

        
            choice = input("Enter your choice (1/2/3/4/5/6): ")

            if choice == "1":
                amount = float(input("Enter the deposit amount: Rs."))
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)
                result = atm.deposit(amount)
                print(f"{result}\npass_code: {pass_code_display}")
            elif choice == "2":
                amount = float(input("Enter the withdrawal amount: Rs."))
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)
                result = atm.withdraw(amount)
                print(f"{result}\npass_code: {pass_code_display}")
            elif choice == "3":
                print("Choose Transfer Type:")
                print("1. Account Transfer")
                print("2. Phone Transfer")
                print("3. Card Transfer")
                transfer_type = int(input("Enter your choice (1/2/3): "))

                
                amount = float(input("Enter the transfer amount: Rs."))
                recipient = input("Enter the recipient's name: ")

                transfer_details = f"Recipient: {recipient}"

                if transfer_type == 1:
                    account_no = input("Enter recipient's account number: ")
                    ifsc_code = input("Enter recipient's account IFSC code: ")
                    pass_code = input("Enter 4 or 6 digit pass_code: ")
                    pass_code_display = '*' * len(pass_code)
                    transfer_details = f"Recipient: {recipient}\nAccount: {account_no}\nIFSC: {ifsc_code}\nPasscode: {pass_code_display}"
                    result = atm.transfer(amount, transfer_details, transfer_type)
                elif transfer_type == 2:
                    phone_number = input("Enter recipient's phone number: ")
                    upi_id = input("Enter UPI ID: ")
                    pass_code = input("Enter 4 or 6 digit pass_code: ")
                    pass_code_display = '*' * len(pass_code)
                    
                    transfer_details = f"Recipient: {recipient}\nPhone: {phone_number}\nUPI: {upi_id}\nPasscode: {pass_code_display}"
                    result = atm.transfer(amount, transfer_details, transfer_type)
                elif transfer_type == 3:
                    card_number = input("Enter recipient's card number: ")
                    pass_code = input("Enter 4 or 6 digit pass_code: ")
                    pass_code_display = '*' * len(pass_code)
                    transfer_details = f"Recipient: {recipient}\nCard: {card_number}\nPasscode: {pass_code_display}"
                    result = atm.transfer(amount, transfer_details, transfer_type)
                else:
                    result = "Invalid transfer type selection."
                    transfer_details = "N/A"
                print(result)
            elif choice == "4":
                balance = atm.get_balance()
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)
                print(f"{balance}\npass_code: {pass_code_display}\nAvailable Balance: Rs.{atm.balance:.2f}")
           
            elif choice == "5":
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)
                atm.pass_code = pass_code
            
               
                history = atm.get_transaction_history()
                
               
                if len(history) > 0:
                    table = []
                    available_balance = atm.initial_balance
                    for i, transaction in enumerate(history, start=1):
                        transaction_parts = transaction.split('Rs.')
                        if len(transaction_parts) > 1:
                            transaction_amount = float(transaction_parts[-1].split()[0])
                            
                    
                            if "Deposited" in transaction:
                                available_balance += transaction_amount
                            elif "Withdrawn" in transaction or "Transferred" in transaction:
                                available_balance -= transaction_amount
                        
                       
                        table.append([i, transaction, f"Rs.{available_balance:.2f}"])
                    print(tabulate(table, headers=["#", "Transaction", "Available Balance"], tablefmt="grid"))
                else:
                    print("Transaction history is empty.")

          
            elif choice == "6":
                print("Thank you for using ATM. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

    
        continue_choice = input("Do you want to perform another transaction? (yes/no): ")
        
        if continue_choice.lower() != "yes":
            print("Thank you for using ATM. Goodbye!")
   
    else:
        print("Invalid User ID or PIN. Exiting...")
        sys.exit() 


if __name__ == "__main__":
    atm_interface()
