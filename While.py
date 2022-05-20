#While exemples
x = 1
while x<10:
    print('The value of x is: ', x)
    x = x+1
else:
    print('The value of x is: ', 10)

#Using more than 1 variable
x = 1
y = 1
while x<10 and y<20:
    print('The value of x*y is ', x*y)
    x = x+1
    y = y+2
else:
    print('The value of x is: ', x*y)

#Using BREAK
x = 1
list1 =[]
while True:
    list1 += [x]
    x += 1
    if x>10:
        print(x)
        print(list1)
        break

#Using CONTINUE
until = 50
x = 0
while x<until:
    x += 1
    if x%2!=0:
        continue
    if x%2==0:
        print(x, 'is pair')


