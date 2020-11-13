from random import randrange

brd2 = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]


def DisplayBoard(board):
    #
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console
    #
    for i in range(3):
        print("+", "-" * 7, "+", "-" * 7, "+", "-" * 7, "+", sep="")
        print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|", sep="")
        print("|", " " * 3, board[i][0], " " * 3, "|", " " * 3, board[i][1], " " * 3, "|", " " * 3, board[i][2],
              " " * 3, "|", sep="")
        print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|", sep="")
    print("+", "-" * 7, "+", "-" * 7, "+", "-" * 7, "+", sep="")


def EnterMove(board):
    #
    # the function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision
    #
    brd = board
    move = int(input("Please select your move"))
    if move < 1 or move > 9:
        print("This move is out of the acceptable range")
        move = int(input("Please re-enter a valid move"))

    if move == 1:
        if brd[0][0] != "X" and brd[0][0] != "O":
            brd[0][0] = "O"
        else:
            print("This square is occupied")
    elif move == 2:
        if brd[0][1] != "X" and brd[0][1] != "O":
            brd[0][1] = "O"
        else:
            print("This square is occupied")
    elif move == 3:
        if brd[0][2] != "X" and brd[0][2] != "O":
            brd[0][2] = "O"
        else:
            print("This square is occupied")
    elif move == 4:
        if brd[1][0] != "X" and brd[1][0] != "O":
            brd[1][0] = "O"
        else:
            print("This square is occupied")
    elif move == 5:
        if brd[1][1] != "X" and brd[1][1] != "O":
            brd[1][1] = "O"
        else:
            print("This square is occupied")
    elif move == 6:
        if brd[1][2] != "X" and brd[1][2] != "O":
            brd[1][2] = "O"
        else:
            print("This square is occupied")
    elif move == 7:
        if brd[2][0] != "X" and brd[2][0] != "O":
            brd[2][0] = "O"
        else:
            print("This square is occupied")
    elif move == 8:
        if brd[2][1] != "X" and brd[2][1] != "O":
            brd[2][1] = "O"
        else:
            print("This square is occupied")
    elif move == 9:
        if brd[2][2] != "X" and brd[2][2] != "O":
            brd[2][2] = "O"
        else:
            print("This square is occupied")

    return brd


def MakeListOfFreeFields(board):
    #
    # the function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    #
    freelst = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                freelst.append((i, j,))
    return freelst


def VictoryFor(board, sign):
    #
    # the function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    #
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
        elif board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
        elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            return True
        elif board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
            return True
        else:
            return False


def DrawMove(board):
    #
    # the function draws the computer's move and updates the board
    #
    brd = board
    while True:
        move = randrange(8)
        if move == 1:
            if brd[0][0] != "X" and brd[0][0] != "O":
                brd[0][0] = "X"
                break
        elif move == 2:
            if brd[0][1] != "X" and brd[0][1] != "O":
                brd[0][1] = "X"
                break
        elif move == 3:
            if brd[0][2] != "X" and brd[0][2] != "O":
                brd[0][2] = "X"
                break
        elif move == 4:
            if brd[1][0] != "X" and brd[1][0] != "O":
                brd[1][0] = "X"
                break
        elif move == 5:
            if brd[1][1] != "X" and brd[1][1] != "O":
                brd[1][1] = "X"
                break
        elif move == 6:
            if brd[1][2] != "X" and brd[1][2] != "O":
                brd[1][2] = "X"
                break
        elif move == 7:
            if brd[2][0] != "X" and brd[2][0] != "O":
                brd[2][0] = "X"
                break
        elif move == 8:
            if brd[2][1] != "X" and brd[2][1] != "O":
                brd[2][1] = "X"
                break
        elif move == 9:
            if brd[2][2] != "X" and brd[2][2] != "O":
                brd[2][2] = "X"
                break

    return brd


DisplayBoard(brd2)
while True:
    brd2 = EnterMove(brd2)
    DisplayBoard(brd2)
    if VictoryFor(brd2, "O"):
        print("You won!")
        break
    brd2 = DrawMove(brd2)
    DisplayBoard(brd2)
    if VictoryFor(brd2, "X"):
        print("Computer Wins!")
        break