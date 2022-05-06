def power_recursive(a,b):
    if b==0:
        return 1
    return a*power_recursive(a,b-1)
print(power_recursive(7,4))