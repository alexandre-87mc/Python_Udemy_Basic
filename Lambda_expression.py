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
pair = lambda x: x%2 ==0
#print lambda functions
print(pair(3))
print(pair(4))

#Lambda function returns first char
firstChar = lambda s: s[0]
print(firstChar('Hola mundo!'))

#Lambda function returns inverted string
invert_string = lambda s: s[::-1]
print(invert_string('John is a very happy man!'))
