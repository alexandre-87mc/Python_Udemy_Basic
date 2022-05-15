#Funcoes
#def define a funcao
def primeira_funcao():
    '''
    Printa "ola mundo"
    '''
    print('Ola mundo!')
primeira_funcao()

#Funcao que soma 2 valores
def somar(num1,num2):
    return num1+num2
somar(1,2)
x = somar(3,3)
print(x)

#Não é necessario definir parâmetros e tipos
st = somar('Oi meu ', 'amigo')
print(st)

#Funcao prova se numero é primo
def primo(num):
    '''
    Método para checar de número é primo
    '''
    for n in range(2,num):
        if num % n == 0:
            print('Não é primo.')
            break
    else:
        print('Primo')
primo(11)

#Se defino funcao dentro de outra funcao
#ela só existe dentro da funcao e nao pode
#ser chamada fora da funcao.