total=0
count=0
while True:
    strn=input('Enter a number:')
    if strn=='done':
        break
    try:
        n=float(strn)
    except:
        print('Invalid input')
    total+=n
    count+=1
    
print(total,count,total/count)
