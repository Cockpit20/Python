max=None
min=None
count=0
sum=0
for i in [23,58,10,4,8]:
    if max is None:
        max=i
    elif i>max:
        max=i
    if min is None:
        min=i
    elif i<min:
        min=i
    sum+=i
    count+=1

print('Largest =',max)
print('Smallest =',min)
print('Sum =',sum)
print('Count =',count)
print('Average =',sum/count)