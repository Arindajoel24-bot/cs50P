text = input("Enter text: ")

for letter in text:
    if letter.lower() in "aeiou":
       text = text.replace(letter, "")

print(text)
  