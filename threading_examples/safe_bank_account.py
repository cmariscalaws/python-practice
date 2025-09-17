import threading
import time

# Thread-safe Bank Account using a Lock with a context manager
class SafeBankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def withdraw(self, amount):
        with self.lock:
            # The 'with' statement ensures this block of code is
            # executed by only one thread at a time.
            if self.balance >= amount:
                time.sleep(0.01) # Simulate a delay
                self.balance -= amount
                print(f"{threading.current_thread().name}: Withdrawal successful. New balance is {self.balance}")
            else:
                print(f"{threading.current_thread().name}: Insufficient funds.")

def safe_withdrawal(account, amount):
    account.withdraw(amount)

# --- Thread-Safe Withdrawal Demonstration ---
if __name__ == "__main__":
    print("--- Safe Withdrawal Example ---")
    safe_account = SafeBankAccount(100)

    # Create two threads to withdraw $75 each
    t3 = threading.Thread(target=safe_withdrawal, args=(safe_account, 75), name="Thread-3")
    t4 = threading.Thread(target=safe_withdrawal, args=(safe_account, 75), name="Thread-4")

    t3.start()
    t4.start()

    t3.join()
    t4.join()

    print(f"Final balance of the safe account: {safe_account.balance}")

    # The final balance will be $25. One thread will succeed, and the other
    # will correctly report insufficient funds because the lock ensured
    # the operations were serialized.
