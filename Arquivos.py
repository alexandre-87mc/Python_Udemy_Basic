#Arquivos
my_file = open('texto.txt', 'w')
my_file.write('banana\n')
my_file.write('só presta a caturra')
my_file.close()
my_file = open('texto.txt', 'r')
print(my_file.name)
conteudo = my_file.read()
print(conteudo)
my_file.close()