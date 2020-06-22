num = int(input("Give me a number, and I'll tell you if it's even or odd: "))

def decision(n):
    if n % 2 == 0:
        if n % 4 == 0:
            print("Even & Divisble by 4.")
        else:
            print("Even number.")    
    else:
        print("Odd number.")        

decision(num)

print("Now let's check if two number are divisable.")
n1 = int(input("1st number: "))
n2 = int(input("2nd number: "))

def devisable(n1,n2):
    if n1 % n2 == 0: 
        print(str(n1) + " is divisable by " + str(n2))
    if n2 % n1 == 0: 
        print(str(n2) + " is divisable by " + str(n1))
    if n1 % n2 != 0 and n2 % n1 != 0:
        print("Not divisable.")    

devisable(n1,n2)