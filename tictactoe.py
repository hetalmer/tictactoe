import random
x = [' ' for x in range(9)]
y = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [0, 3, 6], [2, 4, 7], [2, 5, 8]]
def isfull():
        return ' ' not in x
def iswinner(symbol):
    flag = True
    for i in range(0, len(y)):
        if x[y[i][0]] == x[y[i][1]] == x[y[i][2]] == symbol:
            flag = True
            break
        else:
            flag = False
    return flag
def checkavailibility(pos):
    return x[pos] == ' '
def printmatrix():
    for i in range(0, len(x)):
        print('|  '+str(x[i])+'  |', end="")
        if i == 2 or i == 5 or i == 8:
            print('\n')
def insertletter(pos, letter, x):
    x[pos] = letter
    printmatrix()
def findplace():
    for i in range(0,len(y)):
        if x[y[i][0]] =='O' and x[y[i][1]] == 'O' and x[y[i][2]] == ' ':
            return y[i][2]
        elif x[y[i][1]] == 'O' and x[y[i][2]] == 'O' and x[y[i][0]] == ' ':
            return y[i][0]
        elif x[y[i][0]] == 'O'  and x[y[i][2]] == 'O' and x[y[i][1]] == ' ':
            return y[i][1]
    for i in range(0,len(y)):
        if x[y[i][0]] == 'X' and x[y[i][1]] == 'X' and x[y[i][2]] == ' ':
            return y[i][2]
        elif x[y[i][1]] == 'X' and x[y[i][2]] == 'X' and x[y[i][0]] == ' ':
            return y[i][0]
        elif x[y[i][0]] == 'X' and x[y[i][2]] == 'X' and x[y[i][1]] == ' ':
            return y[i][1]
    return -1
def coumputerturn():
    pc = findplace()
    if pc != -1:
        insertletter(pc, 'O', x)
    if pc == -1:
        flag = 1
        while flag == 1:
            n = random.randint(0, 8)
            if checkavailibility(n) == True:
                insertletter(n, 'O', x)
                flag = 0
choice = 1
printmatrix()
while choice != -1:
    if choice == 1:
        pos = int(input("Enter the position between 1 to 9 on which you want to put X"))
        if (pos >= 1 and pos <= 9):
            if checkavailibility(pos-1):
                insertletter(pos-1, 'X', x)
                choice = 0
                if iswinner('X'):
                    print('You won the game')
                    break
            else:
                print("Entered position is already occupied")
        else:
            print('Entered position out of range plz enter proper position')
    elif choice == 0:
        coumputerturn()
        choice = 1
        if iswinner('O'):
            print('Computer won the game')
            break
    if isfull():
        choice = -1
        print('Tie game')
