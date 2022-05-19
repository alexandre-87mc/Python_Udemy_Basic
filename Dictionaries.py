#Dictionaries

#Declare, initialize and print list
list1 = [1,2,3]
print(list1[1])

#Declare, initialize and print dictionary
Dictio = {'Key1':1.2, 'asdasd':'string', 'Key2':[1,2,[1,2,3]]}
print(Dictio)

#Print dictionary itens
print(Dictio['asdasd'])
print(Dictio['Key2'][2][1])

#Dictionaries are mutable
Dictio['Key1'] = 'Xuxu'
print(Dictio)

#Dictionaries can receive keys
Dictiox = {}
print(Dictiox)
Dictiox['k1'] = 'dog1'
Dictiox['k2'] = 'dog2'
print(Dictiox)

#We can have dictionaries inside dictionaries
Dictiox['in_dicionary'] = Dictio
print(Dictiox)

#Dictionaries methods
print(Dictio.keys())
print(Dictio.values())
print(Dictio.items())
