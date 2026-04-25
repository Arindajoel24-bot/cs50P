camelCase = input("Enter camelCase: ")

snake_case = []

for letter in camelCase:
    if letter == letter.upper():
        snake_case.append("_" + letter.lower())
    elif letter == letter.lower():
        snake_case.append(letter.lower())

print("".join(snake_case))

    
