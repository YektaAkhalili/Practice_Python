def divisors(n):
    l_divisors = []
    for i in range(0,100):
        l_divisors.append(n * i)
    return l_divisors 

number = int(input("Enter a number lower than 100"))

print(divisors(number))
