import json
import re
import pandas as pd

def parse_move_string(move_string):
    pattern = r"move (\d+) from (\d+) to (\d+)"
    match = re.match(pattern, move_string)

    if match:
        amount = int(match.group(1))
        from_position = int(match.group(2)) - 1
        to_position = int(match.group(3)) - 1
        return amount, from_position, to_position

    return None


def main():
    marker = ""
    data = []
    count = 0
    with open(r"C:\Users\praktikant_2\Downloads\AoC Five.json") as f:
        lines = f.readlines()



    stack_lines = lines[:lines.index('\n') - 1]
    instruction_lines = lines[lines.index("\n") +1 :]


    index = 1
    while index < len(stack_lines[0]):
        data.append([])
        for line in stack_lines.__reversed__():
            if line[index] == " ":
                break
            data[-1].append(line[index])
        index += 4


    print(data)

    for l in instruction_lines:
        amount, from_position, to_position = parse_move_string(l)
        hold = []
        for i in range(amount):
            hold.append(data[from_position].pop())
        for j in hold.__reversed__():
            data[to_position].append(j)

    for ar in data:
            print(ar[-1])

if __name__ == "__main__":
    main()