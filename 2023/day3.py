import re

from common import read_file_to_list


# The engine schematic (your puzzle input) consists of a visual representation of the engine
# any number adjacent to a symbol, even diagonally, is a "part number" and should be included
# find engine part numbers
# What is the sum of all of the part numbers in the engine schematic?
def algo_part_one(input_file_name) -> int:
    print("running algo part one..." + input_file_name)
    grid = read_file_to_list(input_file_name)

    symbols = ['*', '$', '#', '@', '-', '%', '&', '/', '=', '+']
    valid_part_numbers = list()
    for y, row in enumerate(grid):

        for part_number_match in re.finditer(r"\d+", row):
            start_idx = part_number_match.start()
            end_idx = part_number_match.end()
            part_number = int(row[start_idx:end_idx])

            # collect all characters around this number
            # if one of those characters is a symbol
            # then add part number to valid part numbers set
            neighbours = set()
            if start_idx > 0:
                preceding_char = row[start_idx - 1: start_idx]
                neighbours.add(preceding_char)
            if end_idx + 1 < len(row):
                succeeding_char = row[end_idx: end_idx + 1]
                neighbours.add(succeeding_char)
            if y + 1 < len(grid):
                row_below = grid[y + 1]
                neighbours = neighbours | set(row_below[start_idx:end_idx])
            if y > 0:
                row_above = grid[y - 1]
                neighbours = neighbours | set(row_above[start_idx:end_idx])
            # diagonal, bottom right
            if y + 1 < len(grid) and end_idx + 1 < len(row):
                neighbours.add(grid[y + 1][end_idx])
            # diagonal, bottom left
            if y + 1 < len(grid) and start_idx > 0:
                neighbours.add(grid[y + 1][start_idx - 1])
            # diagonal, top right
            if y > 0 and end_idx + 1 < len(row):
                neighbours.add(grid[y - 1][end_idx])
            # diagonal, top left
            if y > 0 and start_idx > 0:
                neighbours.add(grid[y - 1][start_idx - 1])

            for n in neighbours:
                if n in symbols:
                    valid_part_numbers.append(part_number)

    return sum(valid_part_numbers)


# A gear is any * symbol that is adjacent to exactly two part numbers
# Its gear ratio is the result of multiplying those two numbers together
def algo_part_two(input_file_name) -> int:
    print("running algo part two..." + input_file_name)
    grid = read_file_to_list(input_file_name)

    gear_symbol = '*'
    for y, row in enumerate(grid):

        for part_number_match in re.finditer(r"\d+", row):
            start_idx = part_number_match.start()
            end_idx = part_number_match.end()
            part_number = int(row[start_idx:end_idx])

            # collect all gears with all adjacent part numbers
            # preceding char
            if start_idx > 0:
                check_for_gear_symbol_at(y, start_idx - 1, grid, part_number)

            # succeeding char
            if end_idx + 1 < len(row):
                check_for_gear_symbol_at(y, end_idx, grid, part_number)

            if y + 1 < len(grid):
                row_below = grid[y + 1]
                row_part_below = row_below[start_idx:end_idx]
                # find out exact position of *
                if gear_symbol in row_part_below:
                    offset = row_part_below.find(gear_symbol)
                    key = str(y + 1) + '_' + str(start_idx + offset)
                    update_gear_map(key, part_number)

            if y > 0:
                row_above = grid[y - 1]
                row_part_above = row_above[start_idx:end_idx]
                # find out exact position of *
                if gear_symbol in row_part_above:
                    offset = row_part_above.find(gear_symbol)
                    key = str(y - 1) + '_' + str(start_idx + offset)
                    update_gear_map(key, part_number)

            # diagonal, bottom right
            if y + 1 < len(grid) and end_idx + 1 < len(row):
                check_for_gear_symbol_at(y + 1, end_idx, grid, part_number)

            # diagonal, bottom left
            if y + 1 < len(grid) and start_idx > 0:
                check_for_gear_symbol_at(y + 1, start_idx - 1, grid, part_number)

            # diagonal, top right
            if y > 0 and end_idx + 1 < len(row):
                check_for_gear_symbol_at(y - 1, end_idx, grid, part_number)

            # diagonal, top left
            if y > 0 and start_idx > 0:
                check_for_gear_symbol_at(y - 1, start_idx - 1, grid, part_number)

    # PHASE 2
    gear_ratios = list()
    for key, part_numbers in gears_with_part_numbers.items():
        # valid gear is adjacent to exactly two part numbers
        # Its gear ratio is the result of multiplying those two numbers together
        if len(part_numbers) == 2:
            gear_ratios.append(part_numbers[0] * part_numbers[1])

    return sum(gear_ratios)


def check_for_gear_symbol_at(y, x, grid, part_number):
    if grid[y][x] == '*':
        key = str(y) + '_' + str(x)
        update_gear_map(key, part_number)


def update_gear_map(key: str, part_number: int):
    if not gears_with_part_numbers.get(key):
        gears_with_part_numbers[key] = [part_number]
    else:
        parts = gears_with_part_numbers.get(key)
        parts.append(part_number)
        gears_with_part_numbers[key] = parts


if __name__ == '__main__':
    day = 3
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 4361 == algo_part_one(test_input_file)
    # print(f'result: {algo_part_one(input_file)}')
    assert 532331 == algo_part_one(input_file)
    # part 2
    gears_with_part_numbers = dict()
    assert 467835 == algo_part_two(test_input_file)
    gears_with_part_numbers.clear()
    assert 82301120 == algo_part_two(input_file)
