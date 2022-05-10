numbers=[34,243,659,517,8,47]
def twistNumbers(n):
    s=0
    b=n
    while b>0:
        digit=b%10
        s=s*10+digit
        b=int(b/10)
    return 2*s

for i in range(len(numbers)):
    numbers[i]=twistNumbers(numbers[i])
    
print(numbers)