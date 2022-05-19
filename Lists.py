#Lists - testes

#Declare, initialize an print list
my_list = [1,2,3]
print(my_list)

#Declare, initialize an print list
my_list2 = [1,2,3,'string']
print(my_list2)

#Print items, sum two lists, multiply list, count list items
print(my_list[0])
print(my_list + my_list2)
print(my_list*10)
print(len(my_list))
a = my_list.count(1)
print(a)

#insert item in list, remove item from list
my_list.append('john')
print(my_list)
my_list.pop(3)
print(my_list)

#Invert list, create a list of lists = matrix
nova_list =['a',3,'d']
print(nova_list)
nova_list.reverse()
print(nova_list)
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
matrix = [list1, list2, list3]
print(list1, list2, list3)
print(matrix)
print(len(matrix))
print(matrix[1][2])

#print list collum
col1 = [row[0] for row in matrix]
print(col1)
