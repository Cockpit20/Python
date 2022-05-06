n=122
b=n
print(b)
s=0
while b>0:
    digit=b%10
    s=s*10+digit
    b=int(b/10)
if n==s:
    print(n,'is palindrome')
else:
    print(n,'is not palindrome')
