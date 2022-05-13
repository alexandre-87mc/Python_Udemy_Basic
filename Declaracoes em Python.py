#Declarações em Python
a = 1
b = 11
if a>b:
    print('Sim, %i é maior que %i' %(a,b))
else:
    print('Não, %i não é maior que %i' %(a,b))

#Testes com If e elif
lista = [1,2,3,4,5,6,7,8,9,10]
if lista[3] >= 9:
    print('Aprovado!')
elif lista[5] <= 6:
    print('Reprovado!')
else:
    print('Não sei mais o que fazer.')

#Declaração de um dicionario
Dicionario = {'Adriano':10,'Paulo':7,'Joao':3}
j='Adriano'
k='Paulo'
l='Joao'

#Testes com if else
if Dicionario[j] >= 9:
    print('Parabéns! Você foi ótimo!')
if Dicionario[k] >= 6:
    print('Parabéns, você passou!')
if Dicionario[l] >= 6:
    print('Parabéns, você passou!')
else:
    print("Que pena, você não passou!")