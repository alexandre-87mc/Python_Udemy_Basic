#Nested declarations and scope
x = 25
def printer():
    x = 50
    return x

print(x)
print(printer())

#Rule - LEGB
    #Local
    #Enclosing functions
    #Global
    #Built-in

#Local - X is local
f = lambda x: x**2

#Local encapsulating
name = 'This is a global name' #GLOBAL

def greet():
    name = 'Sammy' #Local

    def hello():
        print('Hello ' +name) #LEGB -> LE

    hello()
greet() #Local encapsulated 
print(name) #Global

#Exemple of variables manipulation and scope
x = 10
def func(x):
    print('The value of x is: ', x)
    x = 2
    print('The value of local x is: ', x)

func(x)
print('The global value of x, still is: ', x)

