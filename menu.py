TOP_MENU = "====== Password Generator ======"
BOT_MENU = "================================"

def menu():
    print("\n")
    print(TOP_MENU)
    print("1: Generate password")
    print("0: Exit")
    print(BOT_MENU)
    return int(input("What do you want to do ?  "))


def getLength():
    length = int(input("Enter password length (12 min)   "))
    if length < 12: length = 12
    return length
