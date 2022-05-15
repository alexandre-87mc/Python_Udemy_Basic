#Teste com funcoes e métodos
#1 - Escreva funcao que calcula volume de 
#esfera dado o seu raio
def Vol_esfera(raio):   #calcula volume def comum
    pi = 3.14
    return pi*raio**2
print(Vol_esfera(2))

Vol_esfera2 = lambda raio: 3.14*raio**2 #utilizando funcao lambda
print(Vol_esfera2(2))

#2 - Escreva funcao que verifica se um
#numero esta em determinado intervalo
def P0_a_P50(num): #Verifica se está no intervalo de 0 a 50
    for i in range(0,51):
        if i == num:
            print('Numero fornecido está entre 0 e 50')
            break
    else:
        print('Numero fornecido não está entre 0 e 50')
print(P0_a_P50(30))
print(P0_a_P50(51))

#3 - Escreva uma funcao que aceita uma 
#string e calcula o numero de maiusculas
#e minusculas
def Num_Mai_Num_Min(st):
    l = 0
    u = 0
    for char in st:
        if char.islower():
            print('+1 minuscula')
            print(char)
            l += 1
        elif char.isupper():
            print('+1 maiuscula')
            u += 1
        else:
            continue
    return print('Numero de maiusculas: %r  Numero de minusculas: %r ' %(u,l))
st1 = 'Lorena é uma pessoa alegre'
Num_Mai_Num_Min(st1)


#4 - Escreva uma funcao que recebe uma
#lista e retorna uma nova lista com elementos
#exclusivos da primeira lista
def Retorna_exclusivos(l):
    l_excl = set(l)
    return print(l_excl)
lista = [1,2,2,2,3,4,5,66,66,8,8,9,90,90,100]
Retorna_exclusivos(lista)

#5 - Escreva uma funcao para multiplicar
#todos os numeros de uma lista
def Mult_2_num_lista(l):
    i=0
    for num in l:
        l[i] = num*2
        i += 1
    return print(l) 
lista_numeros = [1,2,3]
Mult_2_num_lista(lista_numeros)

#6 - Escreva uma funcao que verifica se 
#string passada é uma palindrome
def Id_palindrome(st):
    st2 = st[::-1]
    tam = len(st)
    for i in range(0,tam):
        if st[i] == st2[i]:
            if i == tam-1:
                print('É palindrome')
                break
            continue 
        else:
            print('Não é palindrome')
            break 
    return 0
string_p = 'ana1'
Id_palindrome(string_p)

#7 - Escreva uma funcao que verifica se 
#string passada é uma pangrama - possui todas as letras de 'a' a 'z'
def pang_func(st):
    i = 0
    j = 0
    alfabeto_st = 'abcdefghijklmnopqrstuvxz'
    alfabeto_lt = []
    
    #Cria lista com alfabeto
    for char1 in alfabeto_st:
        alfabeto_lt.append(char1)
    
    #Define tamanho de string e lista de alfabeto
    tam_alf = len(alfabeto_lt)
    tam_str = len(st)

    #Percorre lista de alfabeto e string procurando ocorrencias em ambas
    for i in range(0,tam_alf):
        for j in range(0,tam_str):
            if alfabeto_lt[i] == st[i]:
                alfabeto_lt.pop(i)
                i += 1
                print(len(alfabeto_lt))
                if len(alfabeto_lt) == 0:       #Não funciona perfeitamente ainda
                    print('É pangrama.')
                    break
            else:
                continue
        if len(alfabeto_lt) > 0:
            print('Não é pangrama')   
st3 = '++abcdefghijklmnopqrstuvxz'
pang_func(st3)