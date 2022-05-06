n=15
b=n
print(b)
s=0
while b>0:
    digit=b%10
    s=s+digit*digit*digit
    b=int(b/10)
if n==s:
    print(n,'is armstrong')
else:
    print(n,'is not armstrong')
