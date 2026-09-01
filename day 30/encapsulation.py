class Instagram:
    def _init_(self,username,password):
        self.username = username
        self.__password = password
        self.__post = []
        print(f"Hello {self.username},Welcome to the instagram")

    def getpassword(self):
        return self.__password

    @property
    def accesspost(self):
        return self.__post

    @accesspost.setter
    def accesspost(self,newpost):
        self.__post.append(newpost)

    def setpassword(self,newpassword):
        self.__password = newpassword

    def display(self):
        print(self.username,self._password,self._post)

avinash = Instagram('avinash','avi@gmail.com')
avinash.display()
print(avinash.username)
print(avinash.getpassword())
print(avinash.accesspost)
avinash.setpassword('avi@3452')
print(avinash.getpassword())
avinash.accesspost='chintu.png'
print(avinash.accesspost)