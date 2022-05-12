#Dicionários
list1 = [1,2,3]
print(list1[1])
dicio = {'chave1':1.2, 'asdasd':'string', 'chave2':[1,2,[1,2,3]]}
print(dicio)
print(dicio['asdasd'])
print(dicio['chave2'][2][1])
#Dicionarios sao mutaveis
dicio['chave1'] = 'Xuxuzinho'
print(dicio)
#Dicionarios podem receber chaves
diciox = {}
print(diciox)
diciox['k1'] = 'dog1'
diciox['k2'] = 'dog2'
print(diciox)
#É possível termos dicionários dentro de dicionários
diciox['dicionario_interno'] = dicio
print(diciox)
#Métodos de dicionários
print(dicio.keys())
print(dicio.values())
print(dicio.items())