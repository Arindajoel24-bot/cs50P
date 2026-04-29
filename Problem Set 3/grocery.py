grocery_list = []

try:
    while True:
        
        user = input("").upper()
    
        grocery_list.append(user)
      
except(EOFError, KeyboardInterrupt):
       grocery_list.sort()
       for grocery in grocery_list:
            print(grocery)    
                    


        
       
            