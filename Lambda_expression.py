#Lambda_expression

#Common function def
def square(num):
    result = num**2
    return result
#print function
print(square(2))

#Common function def simplified
def square2(num): return num**2
#print function
print(square2(2))

#Lambda function returns square number 
square3 = lambda num: num**2
#print lambda function
print(square3(2))

#Lambda function returns pair number
par = lambda x: x%2 ==0
#print lambda functions
print(par(3))
print(par(4))

#Lambda function returns first char
primeirochar = lambda s: s[0]
print(primeirochar('Hola mundo!'))

#Lambda function returns inverted string
inverte_string = lambda s: s[::-1]
print(inverte_string('John is a very happy man!'))
