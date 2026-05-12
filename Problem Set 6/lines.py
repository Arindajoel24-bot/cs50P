import sys

count = 0
#prompt the user for a argv commend 1
try:
    if len(sys.argv) == 1:
        print("Too few command-line arguments.")
    elif len(sys.argv) > 2:
        print("Too many command-line arguments.")
    if len(sys.argv) == 2:
        #if the prompt end with .py
        if sys.argv[1].endswith(".py"):
            with open(sys.argv[1], "r") as file:
                for line in file:
                    count += 1
                    if line.strip().startswith("#"):
                        count -= 1
                    if line.strip() == "":
                        count -= 1
                print(count)    
        elif not sys.argv[1].endswith(".py"):
            print("Not a python file")
except FileNotFoundError:
    sys.exit("Too few command-line arguments.")




#count the lines of that program


#donot count comments and whitespaces


#if the prompt doesn't end with .py return not a python file


#if the prompt doesn't exist return file not available