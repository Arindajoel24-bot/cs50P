greeting = input("Greeting: ")

if greeting == "Hello":
    print("$0")
elif greeting.lower().startswith("h"):
    print("$20")
else:
    print("$100")