#Declaracoes aninhadas e escopo
x = 25
def printer():
    x = 50
    return x

print(x)
print(printer())

#Existem opcoes de escopo - Regra LEGB
    #Local
    #Enclosing functions
    #Global
    #Built-in

#Local - X é local
f = lambda x: x**2

#Locais encapsulados
name = 'This is a global name' #GLOBAL

def greet():
    name = 'Sammy' #Local

    def hello():
        print('Hello ' +name) #Segue LEGB -> LE

    hello()
greet() #Local encapsulado
print(name) #Global

#Exemplo de manipulacao de variaveis e escopo
x = 10
def func(x):
    print('O valor de x é: ', x)
    x = 2
    print('O valor local de x agora é: ', x)

func(x)
print('O valor global de x ainda é: ', x)

