#Compreensao em listas
#Exemplo de preenchimento de lista
x = []
for i in range(0,30):
    x += [i]
    print(x)

#Exemplo de preenchimento de lista simplificado
x2 = [i for i in range(0,30)]
print(x2)

x3 = [i*2+10 for i in range(0,15)]
print(x3)

#Listas pares
x = []
for i in range(0,20):
    if i%2==0:
        x += [i]
        print(x)

x4 = [i for i in range(0,10) if i % 2 == 0]
print(x4)

#Listas strings
lista = [letter for letter in 'word']
print(lista)

#Conversão de temperatura ºC para Fahrenheit
celsius = [0,10,15,20,30,50,100]
fahrenheit = [(temp*(9/5)+32) for temp in celsius]
print(fahrenheit)
