import json




def main():
    count = 0
    with open(r"C:\Users\praktikant_2\Downloads\AoC Four.json") as f:
        for areas in f:
            numbers = []
            x = areas.split(",")
            for part in x:
                start, end = map(int, part.split("-"))
                numbers.append(start)
                numbers.append(end)
                if len(numbers) < 4:
                    pass
                else:
                    range_a = (numbers[0], numbers[1])
                    range_b = (numbers[2], numbers[3])
                    if range_a[0] <= range_b[1] and range_b[0] <= range_a[1]:# or range_a[0] >= range_b[0] and range_a[1] <= range_b[1]:
                        count += 1

    print(count)




if __name__ == "__main__":
    main()