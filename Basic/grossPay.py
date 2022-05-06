hours=input("Enter Hours:")
rate=input("Enter Rate:")
try:
    ival_hours=float(hours)
    ival_rate=float(rate)
except:
    print('Error, please enter numeric input')
    quit()

pay=ival_hours*ival_rate
print('Pay:',pay)