from abc import ABC, abstractmethod


class Printer(ABC):

    @abstractmethod
    def print_doc(self):
        pass


class Scanner(ABC):

    @abstractmethod
    def scan_doc(self):
        pass


# Simple printer sirf Print karega
class BasicPrinter(Printer):

    def print_doc(self):
        print("Printing document...")


# Multi-function printer dono kaam karega
class MultiFunctionPrinter(Printer, Scanner):

    def print_doc(self):
        print("Printing document...")

    def scan_doc(self):
        print("Scanning document...")