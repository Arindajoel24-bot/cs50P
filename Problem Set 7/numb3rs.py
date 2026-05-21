
def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        first, second, third, fourth = ip.split(".")
        first = int(first)
        second = int(second)
        third = int(third)
        fourth = int(fourth)
        
        if 0 <= first <= 255 and 0 <= second <= 255 and 0 <= third <= 255 and 0 <= fourth <= 255:
            return True
        
        else: 
            return False
    except ValueError:
        return False

if __name__ == "__main__":
    main()