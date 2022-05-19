#Functions

#def defines a function
def first_function():
    '''
    Print "Hello World"
    '''
    print('Hello World!')
#call function
first_function()

#function sum 2 numbers
def sum_2(num1,num2):
    return num1+num2
#print function return
print(sum_2(1,2))
x = sum_2(3,3)
print(x)

#It's not necessary to define types
st = somar('Oi meu ', 'amigo')
print(st)

#Prime number function
def prime(num):
    #check if it's a prime number
    for n in range(2,num):
        if num % n == 0:
            print('This is not a prime number.')
            break
    else:
        print('Prime')
prime(11)

#If I define a function inside another function
#it only exists inside the function and cannot
# be called outside the function.
