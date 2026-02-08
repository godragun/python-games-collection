import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

class BankAccount:
    def __init__(self, filename="bank_data.txt"):
        self.filename = filename
        self.accounts = self.load_accounts()
    
    def load_accounts(self):
        try:
            with open(self.filename, 'r') as f:
                accounts = {}
                for line in f:
                    acc_num, name, balance = line.strip().split(',')
                    accounts[acc_num] = {
                        'name': name,
                        'balance': float(balance)
                    }
                return accounts
        except FileNotFoundError:
            return {}
    
    def save_accounts(self):
        with open(self.filename, 'w') as f:
            for acc_num, data in self.accounts.items():
                f.write(f"{acc_num},{data['name']},{data['balance']}\n")
    
    def create_account(self):
        print("\nCreate New Account")
        name = input("Enter name: ")
        acc_num = str(len(self.accounts) + 1001)
        self.accounts[acc_num] = {
            'name': name,
            'balance': 0.0
        }
        print(f"Account created! Your account number is: {acc_num}")
        self.save_accounts()
    
    def deposit(self):
        acc_num = input("Enter account number: ")
        if acc_num in self.accounts:
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    self.accounts[acc_num]['balance'] += amount
                    print(f"Deposited ${amount:.2f}")
                    self.save_accounts()
                else:
                    print("Amount must be positive")
            except ValueError:
                print("Invalid amount")
        else:
            print("Account not found")
    
    def withdraw(self):
        acc_num = input("Enter account number: ")
        if acc_num in self.accounts:
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount > 0:
                    if self.accounts[acc_num]['balance'] >= amount:
                        self.accounts[acc_num]['balance'] -= amount
                        print(f"Withdrew ${amount:.2f}")
                        self.save_accounts()
                    else:
                        print("Insufficient funds")
                else:
                    print("Amount must be positive")
            except ValueError:
                print("Invalid amount")
        else:
            print("Account not found")
    
    def check_balance(self):
        acc_num = input("Enter account number: ")
        if acc_num in self.accounts:
            balance = self.accounts[acc_num]['balance']
            name = self.accounts[acc_num]['name']
            print(f"\nAccount: {acc_num}")
            print(f"Name: {name}")
            print(f"Balance: ${balance:.2f}")
        else:
            print("Account not found")

def bank_system():
    bank = BankAccount()
    
    print("🏦 Bank Account System 🏦")
    print("=" * 40)
    
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. List All Accounts")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        elif choice == '1':
            bank.create_account()
        elif choice == '2':
            bank.deposit()
        elif choice == '3':
            bank.withdraw()
        elif choice == '4':
            bank.check_balance()
        elif choice == '5':
            print("\nAll Accounts:")
            for acc_num, data in bank.accounts.items():
                print(f"{acc_num}: {data['name']} - ${data['balance']:.2f}")
        else:
            print("Invalid choice")

# 22. 🪐 Horoscope

if __name__ == "__main__":
    bank_system()
