
while True:
    fuel = input("Fraction: ")
    fraction = fuel.split("/")

    
    try:
        x = int(fraction[0])
        y = int(fraction[1])

        if x > y:
            continue
        
        percentage = round(x/y * 100)
        
        if percentage <= 1:
            print("E")
            break
        elif percentage >= 99:
            print("F")
            break
        else:
            print(f"{percentage}%")
        
        
    except(ValueError, ZeroDivisionError):
           continue