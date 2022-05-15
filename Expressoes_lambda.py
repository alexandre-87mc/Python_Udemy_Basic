#Expressoes lambda
def square(num):
    result = num**2
    return result

print(square(2))

#simplificando
def square2(num): return num**2
print(square2(2))

#Funcao lambda retorna quadrado
square3 = lambda num: num**2
print(square3(2))

#Funcao lambda retorna par
par = lambda x: x%2 ==0
print(par(3))
print(par(4))

#Funcao lambda retorna primeiro char
primeirochar = lambda s: s[0]
print(primeirochar('Hola mundo!'))

#Funcao lambda retorna string invertida
inverte_string = lambda s: s[::-1]
print(inverte_string('Jose é doido'))