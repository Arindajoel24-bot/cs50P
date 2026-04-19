cost = float(input())
tip_percentage = float(input())

tip = cost * (tip_percentage / 100)
print(f"${tip:.2f}")