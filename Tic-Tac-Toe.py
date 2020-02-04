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
