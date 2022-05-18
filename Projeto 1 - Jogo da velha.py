#Projeto 1 - Jogo da velha
#Premissas:
#1 - Criar função que desenha tabuleiro. Mapear posições de marcação.
#2 - Criar função que recebe entrada e escreve em posição correta do tabuleiro.
    #Tratar entradas que não sejam as esperadas.
3# - Criar função que confere resultado do jogo e retorna status - vencedor, empate, continua
4# - Criar função que chama funções, inicia e encerra jogo.
    #Instruções e comunicados

#ESBOÇO DE DESENHO DE JOGO DA VELHA
#               &               &               
#               &               &
#       1       &       2       &       3       
#               &               &
#               &               &
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#               &               &
#               &               &
#       4       &       5       &       6
#               &               &
#               &               &
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#               &               &
#               &               &
#       7       &       8       &       9
#               &               &
#               &               &

#FUNÇÃO DESENHA JOGO DA VELHA - OK
def DESENHO_JOGO(posicaoX,posicao0,st):
    
    #Declara vetores de posicao
    posX = []
    pos0 = []

    #Inicializa strings que desenham tabuleiro
    L1 = '               &               &               '
    L2 = '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
    seg1 = '               '
    seg2 = '&               &'
    seg3 = '               '
    seg4 = '               '
    seg5 = '&               &'
    seg6 = '               '
    seg7 = '               '
    seg8 = '&               &'
    seg9 = '               '

    #Confere comando de posição dado
    if posicaoX != 0:
        posX.append(posicaoX)
    if posicao0 != 0:
        pos0.append(posicao0)
        

    #Desenha seguimentos do tabuleiro e marca se presente posicao 0 e X
    for k in range(0,18):
        if len(pos0) != 0:
            for i in pos0:
                if i == 1:
                    seg1 = '       0        '
                elif i == 2:
                    seg2 = '&      0        &'
                elif i == 3:
                    seg3 = '       0        '
                elif i == 4:
                    seg4 = '       0        '
                elif i == 5:
                    seg5 = '&      0        &'
                elif i == 6:
                    seg6 = '       0        '
                elif i == 7:
                    seg7 = '       0        '
                elif i == 8:
                    seg8 = '&      0        &'
                elif i == 9:
                    seg9 = '       0        '
        if len(posX) != 0:
            for i in posX:
                if i == 1:
                    seg1 = '       X       '
                elif i == 2:
                    seg2 = '&      X        &'
                elif i == 3:
                    seg3 = '       X        '
                elif i == 4:
                    seg4 = '       X        '
                elif i == 5:
                    seg5 = '&      X        &'
                elif i == 6:
                    seg6 = '       X        '
                elif i == 7:
                    seg7 = '       X        '
                elif i == 8:
                    seg8 = '&      X        &'
                elif i == 9:
                    seg9 = '       X        '

        #Se não há posições nos vetores de posição preenche com posições vazias
        if len(pos0) == 0 and len(posX) == 0:
            if k == 5 or k == 11:
                st = st + L2 + '\n'
            else:
                st = st + L1 + '\n'

        #Se há posições nos vetores de posição preenche com as posições devidas
        else:
            if k == 5 or k == 11:
                st = st + L2 + '\n'
                #print('linha linha printada')
            elif k == 2:
                st = st + seg1 + seg2 + seg3 + '\n'
                #print('linha k=2 printada')
            elif k == 8:
                st = st + seg4 + seg5 + seg6 + '\n'
                #print('linha k=8 printada')
            elif k == 14:
                st = st + seg7 + seg8 + seg9 + '\n'
                #print('linha k=14 printada')
            else:
                st = st + L1 + '\n'
                #print('linha vazia printada')
                #print(st)



    return st


Tabuleiro = ''
print(DESENHO_JOGO(2,9,Tabuleiro))
