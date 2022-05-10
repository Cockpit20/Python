strn=input("Enter the value of n: ")
n=int(strn)
def aidojo(n):
    for i in range(n+1):
        if i%3==0 and i%5!=0:
            print("Ai")
        elif i%5==0 and i%3!=0:
            print("Dojo")
        elif i%3==0 and i%5==0:
            print("AiDojo")
        else:
            print(str(i))
        
aidojo(n)