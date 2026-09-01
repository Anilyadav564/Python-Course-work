from abc import ABC, abstractmethod

class phonepe(ABC):
    def receiverinfo(self):
        print("Enter receiver's details or scanner")
    def amount(self):
        print("Enter the amount")
    def pin(self):
        print("Enter the pin")
    @abstractmethod
    def transaction(self):
        pass
    
class HDFC(phonepe):
    def transaction(self):
        print("Payment using HDFC bank")
class SBI(phonepe):
    def transaction(self):
        print("Payment using SBI bank")
class Union(phonepe):
    def transaction(self):
        print("Payment using Union bank")
class Axis(phonepe):
    def transaction(self):
        print("Payment using Axis bank")
class ICICI(phonepe):
    def transaction(self):
        print("Payment using ICICI bank")
        
viswa=HDFC()
viswa.receiverinfo()
viswa.amount()
viswa.pin()
viswa.transaction()

greesh=SBI()
greesh.receiverinfo()
greesh.amount()
greesh.pin()
greesh.transaction()

cherry=Axis()
cherry.receiverinfo()
cherry.amount()
cherry.pin()
cherry.transaction()