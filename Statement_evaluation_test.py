#Statement evaluation test
#Use for, split() and if to create a statement
#print words that start with s
st = 'Print only the words that star with s in this sentence'
# Break string into word list
list_st = st.split()
print(list_st)
#Select words that start with s
list_st2 = [char for char in list_st if char[0] == 's' or char[0]== 'S']
print(list_st2)

#Use range to print even numbers from 0 to 10
list_pair1 = [i for i in range(0,11) if i%2==0]
print(list_pair1)

#Use list comprehension to create a list of all
#numbers between 1 and 50 that are divisible by 3.
list_div_3 =[div3 for div3 in range(0,51) if div3%3==0]
print(list_div_3)

#Walk through the string below and if the length of a word
#for even, print 'It's even!'
st = 'Print only the words that star with s in this sentence'
lista_word_pair = st.split()
for word in lista_word_pair:
    if len(word)%2==0:
        print(word, 'É par!')

#Use list comprehension to create a list of the
#first letters of each word in the string below
st = 'Print only the words that star with s in this sentence'
split_st = st.split()
list_char1 = [letra[0] for letter in split_st]
print(list_char1)
