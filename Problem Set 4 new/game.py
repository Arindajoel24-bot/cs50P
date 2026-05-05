import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
        
    except ValueError:
        continue

number = random.randint(1, level)

while True:
        try:
            user = int(input("Enter guess: "))
            
            if user < number:
                print("Too small.")
            elif user > number:
                print("Too high.")
            elif user == number:
                print("You guessed right.")
                break
        except ValueError:
            continue