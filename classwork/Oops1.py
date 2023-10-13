class Account:
    def __init__(self, account_id, owner, balance=0):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited Rs{amount} into account {self.account_id}. New balance: Rs{self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew Rs{amount} from account {self.account_id}. New balance: Rs{self.balance}"
        else:
            return "Invalid withdrawal amount."

    def get_balance(self):
        return f"Account {self.account_id} balance: Rs{self.balance}"

    def __str__(self):
        return f"Account ID: {self.account_id}, Owner: {self.owner}, Balance: Rs{self.balance}"


class Transaction:
    @staticmethod
    def transfer(sender, receiver, amount):
        if amount > 0 and sender.balance >= amount:
            sender.withdraw(amount)
            receiver.deposit(amount)
            return f"Transferred Rs{amount} from account {sender.account_id} to account {receiver.account_id}."
        else:
            return "Invalid transfer."


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, owner, initial_balance=0):
        account_id = len(self.accounts) + 1
        account = Account(account_id, owner, initial_balance)
        self.accounts[account_id] = account
        return account

    def get_account(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id]
        else:
            return "Account not found."

    def list_accounts(self):
        return [str(account) for account in self.accounts.values()]


# Example usage:
if __name__ == "__main__":
    bank = Bank("MyBank")

    account1 = bank.create_account("Alice", 1000)
    account2 = bank.create_account("Bob", 500)

    print("Initial account information:")
    print(account1)
    print(account2)

    print(account1.deposit(200))
    print(account2.withdraw(100))

    print(Transaction.transfer(account1, account2, 300))

    print("Updated account information:")
    print(account1)
    print(account2)

    print("All accounts in the bank:")
    print(bank.list_accounts())
