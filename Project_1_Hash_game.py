#Project 1 - Hash game
#HASH GAME PLAN
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

#FUNCTION DRAW THE GAME
def DRAW_GAME(entryX,entry0,st):

    #Declare variables
    posX = []
    pos0 = []

    #Initialize variables
    posX = entryX
    pos0 = entry0
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

    #Draw the table 
    for k in range(0,18):
        if len(pos0) != 0:
            for i in pos0:
                if i == '1':
                    seg1 = '       0       '
                elif i == '2':
                    seg2 = '&      0        &'
                elif i == '3':
                    seg3 = '       0        '
                elif i == '4':
                    seg4 = '       0       '
                elif i == '5':
                    seg5 = '&      0        &'
                elif i == '6':
                    seg6 = '       0        '
                elif i == '7':
                    seg7 = '       0       '
                elif i == '8':
                    seg8 = '&      0        &'
                elif i == '9':
                    seg9 = '       0        '
        if len(posX) != 0:
            for i in posX:
                if i == '1':
                    seg1 = '       X       '
                elif i == '2':
                    seg2 = '&      X        &'
                elif i == '3':
                    seg3 = '       X        '
                elif i == '4':
                    seg4 = '       X       '
                elif i == '5':
                    seg5 = '&      X        &'
                elif i == '6':
                    seg6 = '       X        '
                elif i == '7':
                    seg7 = '       X       '
                elif i == '8':
                    seg8 = '&      X        &'
                elif i == '9':
                    seg9 = '       X        '

        #Print the table without shots
        if len(pos0) == 0 and len(posX) == 0:
            if k == 5 or k == 11:
                st = st + L2 + '\n'
            else:
                st = st + L1 + '\n'

        #Print the players game
        else:
            if k == 5 or k == 11:
                st = st + L2 + '\n'
            elif k == 2:
                st = st + seg1 + seg2 + seg3 + '\n'
            elif k == 8:
                st = st + seg4 + seg5 + seg6 + '\n'
            elif k == 14:
                st = st + seg7 + seg8 + seg9 + '\n'
            else:
                st = st + L1 + '\n'
    return st

def CALL_GAME():

    #Variables declaration
    Tabuleiro = ''
    entryX = []
    entry0 = []
    Winner = 0
    posicaoX = 0
    posicao0 = 0


    #Possibles game combinations
    g1 = ['1','2','3']
    g2 = ['4','5','6']
    g3 = ['7','8','9']
    g4 = ['1','4','7']
    g5 = ['2','5','8']
    g6 = ['3','6','9']
    g7 = ['1','5','9']
    g8 = ['3','5','7']

    #Prints welcome
    print('\nWelcome to the HASH GAME!\n')

    for i in range(0,9):

        #Instruction and input command
        posicaoX = input('Make your input player 1:\n')
        entryX.append(posicaoX)
        print(DRAW_GAME(entryX,entry0,Tabuleiro))
        posicao0 = input('Make your input player 2:\n')
        entry0.append(posicao0)
        print(DRAW_GAME(entryX,entry0,Tabuleiro))

        #If someone made a winner sequence
        if len(entry0)>=3 or len(entryX)>=3: 
            if set(g1).intersection(entryX):
                Winner = 1
            elif set(g1).intersection(entry0):
                Winner = 2
            elif set(g2).intersection(entryX):
                Winner = 1
            elif set(g2).intersection(entry0):
                Winner = 2
            elif set(g3).intersection(entryX):
                Winner = 1
            elif set(g3).intersection(entry0):
                Winner = 2
            elif set(g4).intersection(entryX):
                Winner = 1
            elif set(g4).intersection(entry0):
                Winner = 2
            elif set(g5).intersection(entryX):
                Winner = 1
            elif set(g5).intersection(entry0):
                Winner = 2
            elif set(g6).intersection(entryX):
                Winner = 1
            elif set(g6).intersection(entry0):
                Winner = 2
            elif set(g7).intersection(entryX):
                Winner = 1
            elif set(g7).intersection(entry0):
                Winner = 2
            elif set(g8).intersection(entryX):
                Winner = 1
            elif set(g8).intersection(entry0):
                Winner = 2
            #If there no winners
            elif len(entry0) >= 4 and len(entryX) >= 4 and Winner == 0:
                print('\nEMPATE! JOGUEM NOVAMENTE!\n')
                break
            #Print winner
            if Winner == 1:
                print('\nPlayer 1(x) is the winner!\n')
                break
            elif Winner == 2:
                print('\nPlayer 2(0) is the winner!\n')
                break
            
        #Calls the game printing function
        print('\n'+ DRAW_GAME(entryX,entry0,Tabuleiro))
    return 0

    #Calls the game printing function
    print('\n'+ DRAW_GAME(entryX,entry0,Tabuleiro))

CALL_GAME()
