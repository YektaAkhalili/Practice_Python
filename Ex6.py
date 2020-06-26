def break_up(str):
    str.lower()
    l_forward = []
    l_backward = []
    for i in range(len(str)):
        l_forward.append(str[i])
    for i in range(len(str)-1, -1, -1):
        l_backward.append(str[i])    
    return l_forward, l_backward

def check_palindrome(st1, st2):    
    if st1 == st2:
        print("Palindrome.") 
    else:
        print("Not a palindrome.")    

s = break_up(input("Enter a word:\n"))
p1 = s[0]
p2 = s[1]

check_palindrome(p1,p2)







