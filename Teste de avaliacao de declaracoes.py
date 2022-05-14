#Teste de avaliação de declarações
#Use for, split() e if para criar uma declaração
#que imprima as palavras que começam com s
st = 'Print only the words that star with s in this sentence'
#Quebra string em lista de palavras
lista_st = st.split()
print(lista_st)
#Seleciona palavras que começam com s
lista_st2 = [char for char in lista_st if char[0] == 's' or char[0]== 'S']
print(lista_st2)

#Use range para imprimir numeros pares de 0 a 10
lista_pares1 = [i for i in range(0,11) if i%2==0]
print(lista_pares1)

#Use compreensão de lista para criar uma lista de todos os 
#númeres entre 1 e 50 que são divisíveis por 3.
lista_div_3 =[div3 for div3 in range(0,51) if div3%3==0]
print(lista_div_3)

#Percorra a string abaixo e se o comprimento de uma palavra
#for par, imprima 'É par!'
st = 'Print only the words that star with s in this sentence'
lista_word_par = st.split()
for word in lista_word_par:
    if len(word)%2==0:
        print(word, 'É par!')

#Use compreensão em listas para criar uma lista das
#primeiras letras de cada palavra na string abaixo
st = 'Print only the words that star with s in this sentence'
split_st = st.split()
lista_char1 = [letra[0] for letra in split_st]
print(lista_char1)