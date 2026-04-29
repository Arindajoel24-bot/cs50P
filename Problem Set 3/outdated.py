
d = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        user = input("Date: ") 

        if "/" in user:
            date = user.split("/")

            month = int(date[0])
            day = int(date[1])
            year = int(date[2])

            if month > 12:
                continue
            elif day > 31:
                continue

            print(f"{year}-{month:02}-{day:02}")
            break
        if "," in user:
            date = user.split(" ")
            month = date[0]
            month = d.index(month) + 1
            day = int(date[1].replace(",", ""))
            year = int(date[2])

            if month > 12:
                continue
            elif day > 31:
                continue

            print(f"{year}-{month:02}-{day:02}")
            break
    except:
        continue

        

        




