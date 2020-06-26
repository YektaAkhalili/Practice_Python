a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# this is cheating though! 
a = list(set(a))
b = list(set(b))

new_list = [] 
if len(a) > len(b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                new_list.append(a[i])
                continue
            else: 
                continue    
else:
    for i in range(len(b)): 
        for j in range(len(a)):
            if a[j] == b[i]:
                new_list.append(a[j])
                continue
            else: 
                continue
                  
print(new_list)