expression = input("Expression: ")

x, operator, y = expression.split(" ")

if operator == "+":
    print(float(x) + float(y))
elif operator == "-":
    print(float(x) - float(y))
elif operator == "*":
    print(float(x) * float(y))
elif operator == "/":
    print(float(x) / float(y))
else:
    print("Invalid operator")
    