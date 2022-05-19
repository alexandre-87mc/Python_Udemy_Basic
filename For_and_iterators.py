#For
#Create list
l = [1,2,3,4,5,6,7,8,9,10]

#Print list
print(l)

#For iterate list and prints items multiplied
for num in l:
    print('Num vezes 1:', num)
    print('Num vezes 2:', num *2)
    print('Num vezes 3:', num *3)

#Using For to check if number is pair
for num in l:
    if num % 2 ==0:
        print(num, 'Yes, pair')
    else:
        print(num, 'No, not pair')

#Sum all list items
sum_=0
for num in l:
    sum_ += num
    print(sum_)
print(sum_)

#Using strings
string = 'This is a string'
for char in string:
    print(char)

#Using tuples - print tuple items
tuple1 = (1,2,3,4,5)
for t in tuple1:
    print(t)

#Tuple properties = unpacking
l = [(1,2),(2,3),(3,4)]
(t1,t2)=l[0]
print(t1)
print(t2)
print(t1,t2)
#unpacking
for (t1,t2) in l:
    print(t1*t2)
#print items
for t1 in l:
    print(t1)

#Using dictionaries and printing keys
d = {'k1':1, 'k2':2, 'k3':3}
for item in d:
    print(item)
#Using dictionaries and printing keys and values
for item in d.items():
    print(item)
#Using dictionaries and printing values
for (key,value1) in d.items():
    print(value1)
#Using dictionaries and printing keys and values
for (key,value1) in d.items():
    print(key, ':', value1)

