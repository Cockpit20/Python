print('--------------------------')

astr='Hello Bob'
try:
    istr=int(astr)
except:
    istr=-1
print('First',istr)
astr='123'
try:
    istr=int(astr)
except:
    istr=-1
print('Second',istr)

print('--------------------------')

astr='Bob'
try:
    print('Hello')
    istr=int(astr)
    print('There')
except:
    istr=-1
print('Done',istr);

print('--------------------------')