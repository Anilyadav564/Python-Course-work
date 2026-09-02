class whatsappv1:
    def __init__(self,name):
        self.name=name
        print(f'welcome to the whatsapp-v1{self.name}!')
    def messaging(self):
        print("you can message")          
class whatsappv2(whatsappv1):
    def __init__(self, name):
        self.name=name
        print(f"welcome to the whatsappv2{self.name}!")
    def calls(self):
        print("you can do audio and video calls") 
shiva=whatsappv1('shiva')   
shiva.messaging()   

sai=whatsappv2('sai')
sai.messaging()
sai.calls()