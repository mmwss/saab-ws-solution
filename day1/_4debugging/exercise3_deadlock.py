"""
Fix the deadlock issue in a multi-threaded program
that simulates bank transfers between accounts.
"""

import time, threading

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

def transfer(from_account, to_account, amount):
    # Use a consistent ordering to avoid deadlocks: always acquire locks in the same order
    account1, account2 = (from_account, to_account) if id(from_account) < id(to_account) else (to_account, from_account)

    with account1.lock:
        account1.balance -= amount
        # Simulate some processing delay
        time.sleep(0.1)
        with account2.lock:
            account2.balance += amount

# Example usage
if __name__ == "__main__":
    print("Code Debugging[3] Deadlock Fix")

    # Create accounts
    account_a = BankAccount(1000)
    account_b = BankAccount(1000)

    # Create threads to perform transfers
    t1 = threading.Thread(target=transfer, args=(account_a, account_b, 100))
    t2 = threading.Thread(target=transfer, args=(account_a, account_b, 200))

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()

    print(f"Account A balance: {account_a.balance}")
    print(f"Account B balance: {account_b.balance}")
