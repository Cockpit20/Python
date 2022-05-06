def greet(lang):
    if lang=='es':
        return 'Hola'
    elif lang=='fr':
        return 'Bonjour'
    else:
        return 'Hello'
        
print(greet('en'),'Glenn')
print(greet('es'),'Sally')
print(greet('fr'),'Michael')

def add(a,b):
    sum=a+b
    return sum

sum=add(42,69)
print(sum)

print(max('banana'))