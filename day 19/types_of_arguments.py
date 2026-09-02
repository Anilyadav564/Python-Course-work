#positional arrguments
'''def display(name,email,password):
print(f'name:{name}')
print(f'email:{email}')
print(f'password:{password}')
display('xyz','xyz@gmail.com','xyz@123')
display('xyz@123','xyz@gmail.com','xyz')
display('xyz@gmail.com','xyz@123','xyz')'''
#keyword arrguments
'''def display(name,email,password):
 print(f'name:{name}')
print(f'email:{email}')
print(f'password:{password}')
display('xyz','xyz@gmail.com','xyz@123')
display('xyz@123','xyz@gmail.com','xyz')
display('xyz@gmail.com','xyz@123','xyz')'''
#''''''default argument
'''def display(name,email='gmail.com',password=''):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password:{password}')
display('Anil')'''
#invalid lenth arguments(positional)
'''def display(*names):
    print(names)
display('anil')
display('anil','ganesh')
display('anil','ganesh','avinash')'''
#invalid lenth arguments(keyword )
'''def display(**products):
    print(products)
display(bag=5000)
display(bag=5000,book=30)
display(bag=5000,book=30,bottle=300)'''
