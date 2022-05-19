#Python declarations
a = 1
b = 11
if a>b:
    print('Yes, %i é smaller then %i' %(a,b))
else:
    print('No, %i is not bigger then %i' %(a,b))

#Testes with If and elif
lista = [1,2,3,4,5,6,7,8,9,10]
if lista[3] >= 9:
    print('Aprooved!')
elif lista[5] <= 6:
    print('Failed!')
else:
    print("I don't know.")

#Diccionary declaration
Diccio = {'Adrian':10,'Paul':7,'John':3}
j='Adrian'
k='Paul'
l='John'

#Testes with if else
if Diccio[j] >= 9:
    print('Well done! Great!')
if Diccio[k] >= 6:
    print('Well done! You did it')
if Diccio[l] >= 6:
    print('Well done! You did it')
else:
    print("Too bad you did not pass!")
