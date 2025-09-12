import threading
import time


# Unsafe Bank Account class, prone to race conditions
class UnsafeBankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        # The check and the modification are not atomic
        if self.balance >= amount:
            time.sleep(0.01)  # Simulate a delay to increase the chance of a race condition
            self.balance -= amount
            print(f"Withdrawal successful. New balance is {self.balance}")
        else:
            print("Insufficient funds.")


def unsafe_withdrawal(account, amount):
    account.withdraw(amount)


# --- Race Condition Demonstration ---
if __name__ == "__main__":
    print("--- Unsafe Withdrawal Example ---")
    unsafe_account = UnsafeBankAccount(100)

    # Create two threads to withdraw $75 each
    t1 = threading.Thread(target=unsafe_withdrawal, args=(unsafe_account, 75))
    t2 = threading.Thread(target=unsafe_withdrawal, args=(unsafe_account, 75))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Final balance of the unsafe account: {unsafe_account.balance}")
    print("-" * 35)

    # In many runs, the final balance will be -$50, not $25 or 25, because both
    # threads passed the 'if self.balance >= amount' check before either
    # could update the balance.
