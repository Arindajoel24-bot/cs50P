import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

font = random.choice(figlet.getFonts())

if len(sys.argv) == 1:
    user = input("Input: ")
    figlet.setFont(font=font)
    print(figlet.renderText(user))
    
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid font")
        figlet.setFont(font=sys.argv[2])
        user = input("Input: ")
        print(figlet.renderText(user))
    else:
        sys.exit("Invalid argument")
else:
    print("Invalid Input")

