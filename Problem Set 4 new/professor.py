import random
def main():

    level = get_level()
    score = 0
    
    for _ in range(10):
        number_attempts = 0
        x, y = generate_integer(level)
        

        while True:
            try:
                print(f"{x} + {y} = ", end="")
                answer = int(input(""))
                if answer == x + y:
                    score += 1
                    break
                elif answer < 0:
                    continue
                number_attempts += 1

                if number_attempts == 3:
                    print(f"The correct answer is {x + y}")
                    break
                else:
                    print("EEE")
                    continue
            except ValueError:
                continue
    print(f"Your score is {score}")           

   
def get_level():
 while True:
    try:
        level = int(input("Level: "))
        if level > 3:
            continue
        elif level <= 0:
            continue
        elif level <= 3:
            return level
    except ValueError:
        continue

def generate_integer(level):
    if level == 1:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        return x, y
        
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y
        
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y
        
if __name__ == "__main__":
    main()