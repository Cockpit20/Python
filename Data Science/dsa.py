# Lists (similar to Arrays)
students=['sam','pam','rocky','austin','steve','banner']

for i in range(-6,6):
    print(str(i)+" "+students[i])

students = ['sam', 'pam', 'rocky', 'austin', 'steve', 'banner', 'tony', 'bruce', 'henry', 'clark', 'diana']
student = "Barry"

# Slice Operation
marvel = students[4:7]
flash = student[1:3]

print(marvel)
print(flash)

# slice from the end
dc = students[7:]
flash = student[1:]

print(dc)
print(flash)
# slice from the begining
normal = students[:4]
flash = student[:3]

print(normal)
print(flash)
# length of the list and the string
print(len(students))
print(len(student))