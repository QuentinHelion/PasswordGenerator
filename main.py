from generator import *
from menu import *

choice = 1

while(choice):
    choice = menu()
    if choice == 1:
        length = getLength();
        pwd = generate(length)
        print(pwd)
    elif choice == "0":
        exit()
