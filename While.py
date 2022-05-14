#Exemplos do uso de While
x = 1
while x<10:
    print('O valor de x é', x)
    x = x+1
else:
    print('O valor de x é', 10)

#Utilizando mais de uma variável
x = 1
y = 1
while x<10 and y<20:
    print('O valor de x*y é', x*y)
    x = x+1
    y = y+2
else:
    print('O valor de x é', x*y)

#Utilizando BREAK
x = 1
lista =[]
while True:
    lista += [x]
    x += 1
    if x>10:
        print(x)
        print(lista)
        break

#Utilizando CONTINUE
ate = 50
x = 0
while x<ate:
    x += 1
    if x%2!=0:
        continue
    if x%2==0:
        print(x, 'é par')


