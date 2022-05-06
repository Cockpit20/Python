n=5
index=0
for i in range(n):
    for j in range(i+1):
        print(chr(65+index),"",end="")
        index+=1
    print()