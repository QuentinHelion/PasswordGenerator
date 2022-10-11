TOP_MENU = "====== Password Generator ======"
BOT_MENU = "================================"


# Main menu
def menu(complexity, length):
    print("\n")
    print(TOP_MENU)
    print("Complexity: %s | Length: %s" % (complexity, length))
    print("1: Generate password")
    print("2: Change setting")
    print("0: Exit")
    print(BOT_MENU)
    return int(input("What do you want to do ?  "))

# Setting menu
def setting(complexity, length, nbrOfPwd):
    print("\n")
    print(TOP_MENU)
    print("Complexity: %s | Length: %s | Number of password generated : %s" % (complexity, length, nbrOfPwd))
    print("1: Change length")
    print("2: Change complexity")
    print("3: Change number of password generated")
    print("0: Return")
    print(BOT_MENU)
    return int(input("What do you want to change ?  "))



# === CHANGINGS GENERATOR PARAMETERS MENU ===
# Length changing menu
def changeLength():
    data = int(input("Enter password length (12 min):  "))
    if data < 12:
        print("Too small value ! Length set to 12")
        data = 12
    return data

# Number of password generated changing menu
def changeNbrOfPwd():
    data = int(input("Enter number of password generated per try:  "))
    if data <= 0:
        print("Too small value ! Number set to 1")
        data = 1
    return data

# Complexity changing menu
def changeComplexity():
    print("Complexity of password:\n\
            1 => letter only\n\
            2 => letter + number\n\
            3 => letter + number + punctuation")
    data = int(input("Chose complexity:  "))
    if data < 1 or data > 3 :
        print("Invalid value ! Complexity set to 3")
        data = 3
    return data
