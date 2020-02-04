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

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

turn = "X"

while True:
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
            if len(answer) == 2:
                try:
                    answer = [int(answer[0]) - 1, int(answer[1]) - 1]
                    if board[answer[1]][answer[0]] == " ":
                        board[answer[1]][answer[0]] = "X"
                    else:
                        answer = False
                except:
                    answer = False
            else:
                answer = False
            
        turn = "O"
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
            if len(answer) == 2:
                try:
                    answer = [int(answer[0]) - 1, int(answer[1]) - 1]
                    if board[answer[1]][answer[0]] == " ":
                        board[answer[1]][answer[0]] = "O"
                    else:
                        answer = False
                except:
                    answer = False
            else:
                answer = False
                
        turn = "X"
