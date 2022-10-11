from generator import *
from menu import *

# Password generator object
generator = Generator()

choice = 1
while(choice):

    # Print main menu
    choice = menu(generator.complexity, generator.length)

    # First choice permite to generate and print the password
    if choice == 1:
        generator.create()

    # Add setting feature
    # permite to change length or complexity of password
    elif choice == 2:
        sChoice = 1
        while(sChoice):
            sChoice = setting(generator.complexity, generator.length, generator.nbrOfPwd)
            if(sChoice) == 1:
                generator.setLength(changeLength())
            elif(sChoice) == 2:
                generator.setComplexity(changeComplexity())
            elif(sChoice) == 3:
                generator.setNbr(changeNbrOfPwd())
