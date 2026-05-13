import sys
import csv

#two command-line arguments
try:
    if len(sys.argv) < 3:
        sys.exit("Too few arguments.")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments.")

    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1], "r") as file1:
                with open(sys.argv[2], "w") as file2:
                    input = csv.DictReader(file1)
                    output = csv.DictWriter(file2, fieldnames=("first","last","house"))
                    output.writeheader()
                    header = input.fieldnames
                    for row in input:
                        names = row["name"].split(",")
                        first_name = names[1].strip()
                        #first_name = names[1]
                        last_name = names[0]
                        output.writerow({"first": first_name,"last": last_name, "house":row["house"] })
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a csv file.")                

except FileNotFoundError:
    sys.exit("File not found.")

                
