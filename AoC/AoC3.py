import json

values = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26,

    "A":27,
    "B":28,
    "C":29,
    "D":30,
    "E":31,
    "F":32,
    "G":33,
    "H":34,
    "I":35,
    "J":36,
    "K":37,
    "L":38,
    "M":39,
    "N":40,
    "O":41,
    "P":42,
    "Q":43,
    "R":44,
    "S":45,
    "T":46,
    "U":47,
    "V":48,
    "W":49,
    "X":50,
    "Y":51,
    "Z":52
}
count = 0

def find_duplicates(line):
    duplicates = "a"

    midpoint = len(line) // 2
    first_compartment = line[:midpoint]
    second_compartment = line[midpoint:]

    for char in first_compartment:
        if char in second_compartment and char not in duplicates:
            duplicates = char

    return duplicates


def find_badges(group):
    duplicates = "a"

    first_rucksack = group[0]
    second_rucksack = group[1]
    third_rucksack = group[2]

    for char in first_rucksack:
        if char in second_rucksack and char in third_rucksack:
            duplicates = char

    return duplicates


def main():
    global count

    with open(r"C:\Users\praktikant_2\Downloads\AoC Three.json") as f:
        while True:
            count += values.get(find_badges([next(f).strip() for _ in range(3)]))
            if not count:
                break

            print(count)


if __name__ == "__main__":
    main()