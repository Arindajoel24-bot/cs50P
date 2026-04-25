Amount_due = 50

while True:

 coin = int(input("Insert coin: "))

 if coin == 25:
   Amount_due -= coin
   if Amount_due <= 0:
     print(f"Amount owed: {abs(Amount_due)}")
     break
   print(f"Amount Due: {Amount_due}")
 elif coin == 10:
   Amount_due -= coin
   if Amount_due <= 0:
    print(f"Amount owed: {abs(Amount_due)}")
    break
   print(f"Amount Due: {Amount_due}")
 elif coin == 5:
   Amount_due -= coin
   if Amount_due <= 0:
    print(f"Amount owed: {abs(Amount_due)}")
    break
   print(f"Amount Due:{Amount_due}")

 else:
    print("Invalid")


    
  

