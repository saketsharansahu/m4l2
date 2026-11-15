def palindrome(r):
    e = len(r)-1
    s = 0
    while s < e:
        if r[s] != r[e]:
            return False
        s = s+1
        e = e-1
    return True
r = (1,2,2,0,9,2,1)
print(palindrome(r))
if palindrome(r) == True:
    print("The tuple is a palindrome")
else:
    print("The tuple is not a palindrome")