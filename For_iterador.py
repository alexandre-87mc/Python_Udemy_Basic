#For - introdução
l = [1,2,3,4,5,6,7,8,9,10]

#Print de lista
print(l)

#For que percorre itens em lista
for num in l:
    print('Num vezes 1:', num)
    print('Num vezes 2:', num *2)
    print('Num vezes 3:', num *3)

#Utilizando módulo para determinar numero par
for num in l:
    if num % 2 ==0:
        print(num, 'é par')
    else:
        print(num, 'é impar')

#Realizar somatório
sum_=0
for num in l:
    sum_ += num
    print(sum_)
print(sum_)

#Utilizando strings
string = 'essa é uma string'
for char in string:
    print(char)

#Utilizando tupia
tupia = (1,2,3,4,5)
for t in tupia:
    print(t)

#Propriedade tupia - desembalagem = unpacking
l = [(1,2),(2,3),(3,4)]
(t1,t2)=l[0]
print(t1)
print(t2)
print(t1,t2)
#Desembalagem
for (t1,t2) in l:
    print(t1*t2)
#Exposição
for t1 in l:
    print(t1)

#Utilizando dicionarios e exibindo chaves
d = {'k1':1, 'k2':2, 'k3':3}
for item in d:
    print(item)
#Utilizando dicionarios e exibindo chaves e valores
for item in d.items():
    print(item)
#Utilizando dicionarios e exibindo valores
for (key,valor) in d.items():
    print(valor)
#Utilizando dicionarios e exibindo chaves e valores
for (key,valor) in d.items():
    print(key, ':', valor)

