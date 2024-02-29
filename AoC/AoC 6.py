def has_duplicates(l):
    found = []
    for i in l:
        if i in found:
            return True
        found.append(i)
    return False


def main():
    marker_count = 0
    cache = []
    with open(r"C:\Users\Franky\Downloads\AoC Six.txt") as f:
        input = f.read()



    i = 0

    for i in range(len(input) - 14):
        if len(input) < i + 4: break
        if not has_duplicates(input[i:i + 14]):
            print(i + 14)
            break

if __name__ == "__main__":
    main()