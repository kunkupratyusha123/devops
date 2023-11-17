def ispalindrome(s):
    return s==s[: : -1]
s='pratyusha'
x=ispalindrome(s)
if x:
    print('yes')
else:
    print('no')  
