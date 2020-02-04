import os
os.system("cls")

def clearscreen():
    try:
        os.system("cls")
    except:
        try:
            os.system("clear")
        except:
            pass

def winner():
    global board
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        return "X"
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        return "X"
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        return "X"
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return "X"
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return "X"
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return "X"
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return "X"
    elif board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
        return "X"
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        return "O"
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        return "O"
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        return "O"
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        return "O"
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        return "O"
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        return "O"
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return "O"
    elif board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
        return "O"
    

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

turn = "X"

print("X goes first")
print("Inputs should be 2 digits, the column and the row, seperated by a space")
input()
clearscreen()

won = False

while won == False:
    clearscreen()
    input("Player 1, press ENTER")
    clearscreen()
    while turn == "X":
        answer = False
        while answer == False:
            clearscreen()
            print("   1 2 3")
            print("  +-+-+-+")
            print("1 |" + board[0][0] + "|" + board[0][1] +"|" + board[0][2] + "|")
            print("  +-+-+-+")
            print("2 |" + board[1][0] + "|" + board[1][1] +"|" + board[1][2] + "|")
            print("  +-+-+-+")
            print("3 |" + board[2][0] + "|" + board[2][1] +"|" + board[2][2] + "|")
            print("  +-+-+-+")
            answer = input("Enter your choice now  ")
            if len(answer) == 3:
                try:
                    answer = [int(answer[0]) - 1, int(answer[2]) - 1]
                    if board[answer[1]][answer[0]] == " ":
                        board[answer[1]][answer[0]] = "X"
                    else:
                        answer = False
                except:
                    answer = False
            else:
                answer = False
            
        turn = "O"
    if winner() == "X":
        won = "X"
        break
    clearscreen()
    input("Player 2, press ENTER")
    clearscreen()
    while turn == "O":
        answer = False
        while answer == False:
            clearscreen()
            print("   1 2 3")
            print("  +-+-+-+")
            print("1 |" + board[0][0] + "|" + board[0][1] +"|" + board[0][2] + "|")
            print("  +-+-+-+")
            print("2 |" + board[1][0] + "|" + board[1][1] +"|" + board[1][2] + "|")
            print("  +-+-+-+")
            print("3 |" + board[2][0] + "|" + board[2][1] +"|" + board[2][2] + "|")
            print("  +-+-+-+")
            answer = input("Enter your choice now  ")
            if len(answer) == 3:
                try:
                    answer = [int(answer[0]) - 1, int(answer[2]) - 1]
                    if board[answer[1]][answer[0]] == " ":
                        board[answer[1]][answer[0]] = "O"
                    else:
                        answer = False
                except:
                    answer = False
            else:
                answer = False
                
        turn = "X"
    if winner() == "O":
        won = "O"
        break

clearscreen()
print(won + " won!")
input()
