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
    valid_part_numbers = set()
    for y, row in enumerate(grid):

        for part_number_match in re.finditer(r"\d+", row):
            start_idx = part_number_match.start()
            end_idx = part_number_match.end()
            part_number = row[start_idx:end_idx]
            # print(f'part number: {part_number}')

            # collect all characters around this number
            # if one of those  characters is a symbol
            # then add part number to valid part numbers set
            chars_around = set()
            # before index
            if start_idx > 0:
                preceding_char = row[start_idx - 1: start_idx]
                chars_around.add(preceding_char)
            # after index
            if end_idx + 1 < len(row):
                succeeding_char = row[end_idx: end_idx + 1]
                chars_around.add(succeeding_char)
            # below
            if y + 1 < len(grid):
                next_row = grid[y + 1]
                row_part_below = next_row[start_idx:end_idx]
                chars_around = chars_around | set(row_part_below)
            # above
            if y > 0:
                previous_row = grid[y - 1]
                row_part_above = previous_row[start_idx:end_idx]
                chars_around = chars_around | set(row_part_above)
            # and diagonal, bottom right
            if y + 1 < len(grid) and end_idx + 1 < len(row):
                a = grid[y + 1][end_idx]
                chars_around.add(a)
            # and diagonal, bottom left
            if y + 1 < len(grid) and start_idx > 0:
                a = grid[y + 1][start_idx - 1]
                chars_around.add(a)
            # and diagonal, top right
            if y > 0 and end_idx + 1 < len(row):
                a = grid[y - 1][end_idx]
                chars_around.add(a)
            # and diagonal, top left
            if y > 0 and start_idx > 0:
                a = grid[y - 1][start_idx - 1]
                chars_around.add(a)

            for ca in chars_around:
                if ca in symbols:
                    valid_part_numbers.add(int(part_number))
                    print(f'valid part: {part_number}')

        # for y, col in enumerate(row):
        #     c = grid[x][y]
        #     if c in symbols:
        #         print(f'symbol: {c}')

    return sum(valid_part_numbers)


def algo_part_two(input_file_name) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 3
    debug = False
    trace = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 4361 == algo_part_one(test_input_file)
    # print(f'result: {algo_part_one(input_file)}')
    # assert 42 == algo_part_one(input_file)
    # 328113
    # part 2
    # assert 42 == algo_part_two(test_input_file)
    # print(f'result: {algo_part_two(input_file)}')
    # assert 42 == algo_part_two(input_file)
