''''try:
    a = int(input())
except ValueError:
    print("Enter the correct datatype")
else:
    print("a=",a)
finally:
    print("End of the program")
try: 
    a = int(input("Enter the number: "))
    k = {1: 12, 12: 13}
    l = [232, 54]
except ValueError:
    print('Enter the correct datatype: ')
except KeyError:
    print('Key is not there')
except IndexError:
    print('Index out of range')
except ZeroDivisionError:
    print('Cant divide with zero')
except TypeError:
    print('Enter the correct datatype: ')
except NameError:
    print('Define the variable')
else:
    print("a: ", a)
finally:
    print("Execution completed!!")
    
'''
#
'''try:
    a = int(input("enter:"))
    k = {1:12,12:13}
    #print(k[14])
    l=[232,54]
    print(l[10])
    print(10/0)
    print('1'+1)
except exception as e:
    print("error occured:",e)
else:
    print("error free program")
finally:
    print("end of program")'''
#raise an error
try:
    amount = int(input("enter the amount:"))
    balence = 500
    if amount <0:
        raise Exception("amount needs to br positive")
except Exception as e:
    print("error occured:"e)
else:
    print("error free program")
finally:
    print("end of program")

    
    
    
