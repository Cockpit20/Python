strn=input("Enter a number:")
n=int(strn)
def fib_recursive(n):
    if n==0 or n==1:
        return n
    return fib_recursive(n-1)+fib_recursive(n-2)

print(fib_recursive(n))

for i in range(n+1):
    print(fib_recursive(i),"",end="")