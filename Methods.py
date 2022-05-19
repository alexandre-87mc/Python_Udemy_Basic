#Functions inside objects - some examples of lists methods

#Initialize list, add item, print list, print item index 3, show help, copy list
l = [1,2,3,4,5]
l.append(6)
print(l)
print(l.count(3))
help(l.count)
help(l.clear)
help(l.copy)
l2=[]
l2 = l.copy()
print(l2)
