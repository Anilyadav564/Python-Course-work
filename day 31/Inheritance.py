#single level inheritance
class whatsappv1:
    def messaging(self):
        print("you can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("you can audio and video calls")
a = whatsappv1()
a.messaging()
b = whatsappv2()
b.messaging
b.calls()
#multi level inheritance
class whatsappv1:
    def messaging(self):
        print("you can message")

class whatsappv2(whatsappv1):
    def calls(self):
        print("you can audio and video calls")

class whatsappv3(whatsappv2):
    def status(self):
        print("you can add the status for 24 hours")

b = whatsappv2()
b.messaging()  # inherited from whatsappv1
b.calls()
c = whatsappv3()
c.messaging()
c.calls()
c.status()
#multiple inheritance
class whatsappv1:
    def messaging(self):
        print("you can message")

class whatsappv2:
    def calls(self):
        print("you can audio and video calls")

class whatsappv3(whatsappv1, whatsappv2):
    def status(self):
        print("you can add the status for 24 hours")

c = whatsappv3()
c.messaging()
c.calls()
c.status()
#Hybrid inheritance combines more than one inheritance type.ex :
# Parent class
class whatsappv1:
    def messaging(self):
        print("You can message")

# Single inheritance
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can make audio and video calls")

# Another child of whatsappv1
class whatsapp_status(whatsappv1):
    def status(self):
        print("You can add status for 24 hours")

# Multiple inheritance: inherits from both child classes
class whatsappv3(whatsappv2, whatsapp_status):
    def payments(self):
        print("You can send payments")

a = whatsappv3()

a.messaging()  # from whatsappv1
a.calls()      # from whatsappv2
a.status()     # from whatsapp_status
a.payments()   # from whatsappv3
#Hierarchical inheritance means one parent class has multiple child classes ex:
class whatsappv1:
    def messaging(self):
        print("You can message")

class whatsappv2(whatsappv1):
    def calls(self):
        print("You can make audio and video calls")

class whatsappv3(whatsappv1):
    def status(self):
        print("You can add status for 24 hours")

# Object of whatsappv2
a = whatsappv2()
a.messaging()  # inherited from whatsappv1
a.calls()

# Object of whatsappv3
b = whatsappv3()
b.messaging()  # inherited from whatsappv1
b.status()
#super ex
class whatsappv1:
    def status(self):
        print("You can add images and videos")

class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("You can make audio and video calls")

class whatsappv3(whatsappv2):
    def status(self):
        super().status()
        print("You can  like and you can add reaction")
a = whatsappv3()
a.status()

#Multiple Inheritance and Calling Parent Methods in Python
class whatsappv1:
    def status(self):
        print("You can add images and videos")

class whatsappv2:
    def status(self):
        
        print("You can add misic and  stickers")

class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("You can  like and you can add reaction")
a = whatsappv3()
a.status()

