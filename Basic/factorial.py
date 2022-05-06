def fact_recursive(n):
    if n==0 or n==1:
        return 1
    return n*fact_recursive(n-1)
    
print(fact_recursive(7))