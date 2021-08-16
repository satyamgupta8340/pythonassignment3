# 4.Python function that checks whether a passed string is palindrome or not¶
def ispalindrome(s):
    return s==s[::-1]
s=input('Enter any  string  ')
ans=ispalindrome(s)
if ans:
    print('yes')
else:
    print('no')