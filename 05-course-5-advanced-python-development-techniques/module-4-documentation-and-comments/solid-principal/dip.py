from abc import ABC, abstractmethod


# Abstraction
class MessageService(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


class EmailService(MessageService):

    def send(self, message: str):
        print(f"Sending Email: {message}")


class SMSService(MessageService):

    def send(self, message: str):
        print(f"Sending SMS: {message}")


# High-level module: Abstraction par depend karta hai, concrete class par nahi
class NotificationManager:

    def __init__(self, service: MessageService):
        self.service = service  # Dependency Injection

    def notify(self, message: str):
        self.service.send(message)


# Usage:
email_notifier = NotificationManager(EmailService())
email_notifier.notify("Welcome to Cloud Platform!")