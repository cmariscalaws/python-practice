"""
This module demonstrates the combination of the Strategy and Factory Method design patterns in Python.

Strategy Pattern:
-----------------
The Strategy pattern enables selecting an algorithm's behavior at runtime. Here, different payment methods
(CreditCardStrategy, PayPalStrategy) encapsulate their payment logic in separate classes. The ShoppingCart
context delegates the payment operation to the chosen strategy, allowing the payment method to be changed
dynamically.

Factory Method Pattern:
-----------------------
The Factory Method pattern provides a way to instantiate objects based on input or configuration, without
specifying the exact class of the object that will be created. The payment_factory function acts as a factory,
returning the appropriate payment strategy instance based on the method argument.

How They Work Together:
-----------------------
The factory method is used to create strategy objects, which are then injected into the ShoppingCart context.
This allows the client code to easily switch between payment strategies at runtime, demonstrating the flexibility
and decoupling provided by both patterns.
"""

# The strategies
class CreditCardStrategy:
    def __init__(self):
        print("CreditCardStrategy instance created.")
    def pay(self, amount):
        print("CreditCardStrategy.pay() called.")
        # Payment logic for credit card
        print(f"Paying {amount} via Credit Card.")

class PayPalStrategy:
    def __init__(self):
        print("PayPalStrategy instance created.")
    def pay(self, amount):
        print("PayPalStrategy.pay() called.")
        # Payment logic for PayPal
        print(f"Paying {amount} via PayPal.")

# The factory method for creating payment strategies
def payment_factory(method):
    print(f"payment_factory called with method: {method}")
    strategies = {
        'credit_card': CreditCardStrategy(),
        'paypal': PayPalStrategy(),
    }
    strategy = strategies.get(method)
    if strategy:
        print(f"Factory returning: {strategy.__class__.__name__}")
    else:
        print("Factory returning: None (unknown method)")
    return strategy

# The context using the strategy pattern
class ShoppingCart:
    def __init__(self, amount):
        print(f"ShoppingCart created with amount: {amount}")
        self.amount = amount
        self.payment_strategy = None  # Strategy will be injected

    def set_payment_strategy(self, strategy):
        print(f"set_payment_strategy called with: {strategy.__class__.__name__}")
        """
        Injects the payment strategy into the context.
        Args:
            strategy: An object with a 'pay' method.
        """
        self.payment_strategy = strategy

    def checkout(self):
        print("checkout called.")
        """
        Executes the payment using the selected strategy.
        Raises:
            ValueError: If no payment strategy is set.
        """
        if not self.payment_strategy:
            raise ValueError("Payment strategy not set.")
        self.payment_strategy.pay(self.amount)

# Usage example
if __name__ == "__main__":
    # Manual usage example
    cart = ShoppingCart(150)
    credit_card_payment = payment_factory('credit_card')
    cart.set_payment_strategy(credit_card_payment)
    cart.checkout()
    paypal_payment = payment_factory('paypal')
    cart.set_payment_strategy(paypal_payment)
    cart.checkout()

    # Automated tests with assertions
    import io
    import sys

    def capture_output(func, *args, **kwargs):
        """Helper to capture stdout from a function call."""
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        try:
            func(*args, **kwargs)
        finally:
            sys.stdout = old_stdout
        return buffer.getvalue()

    print( "Test 1: CreditCardStrategy")
    cart1 = ShoppingCart(100)
    cart1.set_payment_strategy(payment_factory('credit_card'))
    output1 = capture_output(cart1.checkout)
    assert "Paying 100 via Credit Card." in output1, f"Unexpected output: {output1}"

    # Test 2: PayPalStrategy
    print("\nTest 2: PayPalStrategy")
    cart2 = ShoppingCart(200)
    cart2.set_payment_strategy(payment_factory('paypal'))
    output2 = capture_output(cart2.checkout)
    assert "Paying 200 via PayPal." in output2, f"Unexpected output: {output2}"

    # Test 3: Switch strategies
    print("\nTest 3: Switch strategies")
    cart3 = ShoppingCart(50)
    cart3.set_payment_strategy(payment_factory('credit_card'))
    output3a = capture_output(cart3.checkout)
    cart3.set_payment_strategy(payment_factory('paypal'))
    output3b = capture_output(cart3.checkout)
    assert "Paying 50 via Credit Card." in output3a, f"Unexpected output: {output3a}"
    assert "Paying 50 via PayPal." in output3b, f"Unexpected output: {output3b}"

    # Test 4: No strategy set
    print("\nTest 4: No strategy set")
    cart4 = ShoppingCart(10)
    try:
        cart4.checkout()
        assert False, "Expected ValueError when no strategy is set."
    except ValueError as e:
        assert str(e) == "Payment strategy not set.", f"Unexpected error message: {e}"

    print("All tests passed.")
