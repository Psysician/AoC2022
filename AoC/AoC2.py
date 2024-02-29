import json

input = 0
X = 1
Y = 2
Z = 3



def main():
    score = 0
    with open(r"C:\Users\praktikant_2\Downloads\AoC Two.json") as f:
        for line in f:

            enemy_choice = line[0]
            my_choice = line[2]

            if my_choice == "X":
                if enemy_choice == "A":
                    score += 3
                elif enemy_choice == "B":
                    score += 1
                elif enemy_choice == "C":
                    score += 2

            elif my_choice == "Y":
                if enemy_choice == "A":
                    score += 4
                elif enemy_choice == "B":
                    score += 5
                elif enemy_choice == "C":
                    score += 6

            elif my_choice == "Z":
                if enemy_choice == "A":
                    score += 8
                elif enemy_choice == "B":
                    score += 9
                elif enemy_choice == "C":
                    score += 7


    print(score)

if __name__ == "__main__":
    main()