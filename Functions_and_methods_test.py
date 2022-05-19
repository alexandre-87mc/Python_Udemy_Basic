#Functions and methods test
#1 - Write a function that calculates the volume of a sphere
def Vol_sphere(radius1):   #sphere volume commum def
    pi = 3.14
    return pi*radius1**2
print(Vol_sphere(2))

Vol_sphere2 = lambda radius2: 3.14*radius2**2 #using lambda function
print(Vol_sphere2(2))

#2 - Write a function that checks if a number is in a range
def P0_a_P50(num): #check if number is in 0 to 50 range
    for i in range(0,51):
        if i == num:
            print('The number is between 0 and 50')
            break
    else:
        print('The number is not between 0 and 50')
print(P0_a_P50(30))
print(P0_a_P50(51))

#3 - Write a function that takes a string and calculate 
#the number of uper and lower case chars
def Num_upp_Num_low(st):
    l = 0
    u = 0
    for char in st:
        if char.islower():
            l += 1
        elif char.isupper():
        else:
            continue
    return print('Number upper chars: %r  Number lower chars: %r ' %(u,l))
st1 = 'Lorena is beautiful'
Num_upp_Num_low(st1)


#4 - Write a function that receives a list and return 
#a new list only with the excluse items from the list
def Only_exclusives(l):
    l_excl = set(l)
    return print(l_excl)
list_ex = [1,2,2,2,3,4,5,66,66,8,8,9,90,90,100]
Only_exclusives(list_ex)

#5 - Write a function that multiplies all the number from a list
def Mult_2_num_list(l):
    i=0
    for num in l:
        l[i] = num*2
        i += 1
    return print(l) 
list_num1 = [1,2,3]
Mult_2_num_list(list_num1)

#6 - Write a function tha verifies if a string is a palindrome
def Id_palindrome(st):
    st2 = st[::-1]
    tam = len(st)
    for i in range(0,tam):
        if st[i] == st2[i]:
            if i == tam-1:
                print('Yes, palindrome')
                break
            continue 
        else:
            print('No, not a palindrome')
            break 
    return 0
string_p = 'ana1'
Id_palindrome(string_p)

#7 - Write a function that verifies if a string is a pangram
def pang_func(st):
    i = 0
    j = 0
    alphabet_st = 'abcdefghijklmnopqrstuvxz'
    alphabet_lt = []
    
    #Cria lista com alfabeto
    for char1 in alphabet_st:
        alphabet_lt.append(char1)
    
    #Define tamanho de string e lista de alfabeto
    tam_alf = len(alphabet_lt)
    tam_str = len(st)

    #Go throug alphabet 
    for i in range(0,tam_alf):
        for j in range(0,tam_str):
            if alphabet_lt[i] == st[i]:
                alphabet_lt.pop(i)
                i += 1
                print(len(alphabet_lt))
                if len(alphabet_lt) == 0:       #Not working yet
                    print('É pangrama.')
                    break
            else:
                continue
        if len(alphabet_lt) > 0:
            print('Not a pangram')   
st3 = '++abcdefghijklmnopqrstuvxz'
pang_func(st3)
