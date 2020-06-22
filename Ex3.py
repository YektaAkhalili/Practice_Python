n = int(input("Enter a number: "))

l_nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_l = [] 

def new_list(n,l):
    for i in range(len(l)):
        if l[i] < n:
            new_l.append(l[i])
        else:
            continue 
    return new_l

print(new_list(n,l_nums))
