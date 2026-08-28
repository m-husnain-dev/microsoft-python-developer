from abc import ABC, abstractmethod


# Abstract base class
class PaymentProcessor(ABC):

    @abstractmethod
    def process(self, amount: float):
        pass


# Existing functionality
class CreditCardPayment(PaymentProcessor):

    def process(self, amount: float):
        print(f"Processing ${amount} via Credit Card.")


# Naya payment method add karne ke liye purana code change nahi karna pada
class JazzCashPayment(PaymentProcessor):

    def process(self, amount: float):
        print(f"Processing ${amount} via JazzCash.")