from __future__ import annotations
import re

def visibility_check_row(grid, row, column):
    if row == 0 or column == 0:
        return 1

    visibility = True

    #left check
    for i in range(len(grid)):
        if i < row:
            if grid[i][column] >= grid[row][column]:
                visibility = False
                break

    if visibility == True:
        return 1

    visibility = True

    #up check
    for i in range(len(grid)):
        if i > row:
            if grid[i][column] >= grid[row][column]:
                visibility = False
                break


    if visibility == True:
        return 1
    else:
        return 0
        

def visibility_check_column(grid, row, column):
    if row == 0 or column == 0:
        return 1

    visibility = True

    #right check
    for i in range(len(grid[0])):
        if i < column:
            if grid[row][i] >= grid[row][column]:
                visibility = False
                break


    if visibility == True:
        return 1

    visibility = True

    #down check
    for i in range(len(grid[0])):
        if i > column:
            if grid[row][i] >= grid[row][column]:
                visibility = False
                break

    if visibility == True:
        return 1
    else:
        return 0



def calc_scenic(x):
    current_tree = -1
    i = 0
    count = 0
    while x[0] >= current_tree and i<=len(x):

        i += 1
        current_tree = x[i]
        count += 1

    return count

def calc_scenic2(list):
    count = 0
    for i,ele in enumerate(list):
        if i == 0:
            continue
        if ele>=list[0]:
            if count == 0:
                return 1
            count += 1
            return count
        count += 1
    if count == 0:
        return 1
    return count



def main():
    grid = []
    count = 0
    row = []

    with open(r"C:\Users\praktikant_2\Downloads\AoC Eight.txt") as f:

        for line in f:
            for nr in line:
                if nr == "\n":
                    pass
                else:
                    row.append(nr)
            grid.append(row)
            row = []

    row = 0
    column = 0
    acu = 0

    print(grid)

    for row_id,row in enumerate(grid):
        for column_id, _ in enumerate( row):

            if visibility_check_row(grid, row_id, column_id) == 1 or visibility_check_column(grid, row_id, column_id) == 1:
                    count += 1

            east = row[column_id:]
            west = row[:column_id+1]
            west.reverse()
            col = [ row[column_id] for row in grid]
            south = col[row_id:]
            north = col[:row_id+1]
            north.reverse()

            score = (calc_scenic2(east)*calc_scenic2(west)*calc_scenic2(north)*calc_scenic2(south))

            if score > acu:
                acu = score


    print(count)
    print(acu)



if __name__ == "__main__":
    main()