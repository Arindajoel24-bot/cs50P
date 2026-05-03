import inflect

p = inflect.engine()

list_names = []
p.join(list_names)
try:
    while True:
        user = input("Enter names: ").title()
        list_names.append(user)
        
except EOFError:
    print(f"Adieu, adieu, to {p.join(list_names)}")




"""
list_names = []
try:
    while True:
        names = input("Enter names: ").title()
        list_names.append(names)
    
except(EOFError, KeyboardInterrupt):
        if len(list_names) == 1:
           print(f"Adieu, adieu, to {list_names[0]}")
        elif len(list_names) == 2:
             print(f"Adieu, adieu, to {list_names[0]} and {list_names[1]}")
        else:
            output = ", ".join(list_names[:-1]) + ", and " + list_names[-1]
            print(f"Adieu, adieu, to {output}")
    """