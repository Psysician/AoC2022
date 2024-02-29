import json
biggest = 0
calc = 0
first = 0
second = 0
third = 0
with open(r"C:\Users\praktikant_2\Downloads\AoC One.json") as f:
    for item in f:
        item = item.strip()
        

        if item == "":
            if calc > first:
                third = second
                second = first
                first = calc
                calc = 0
            elif calc > second:
                third = second
                second = calc
                calc = 0
            elif calc > third:
                third = calc
                calc = 0

            else:
                calc = 0

        if item != "":
            calc += int(item)


print(first+second+third)

