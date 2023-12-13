import re

from common import read_file_to_list
import numpy as np


# --- Day 13: Point of Incidence ---
# You note down the patterns of ash (.) and rocks (#) that you see
# as you walk (your puzzle input); perhaps by carefully analyzing these patterns,
# you can figure out where the mirrors are
def algo_part_one(input_file_name: str) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)

    result = 0
    test_set = []
    test_set_id = 1
    for line in lines:
        if line.strip() != '':
            test_set.append(line)
        else:
            result += run_algo(test_set, test_set_id)
            test_set = []
            test_set_id += 1
    result += run_algo(test_set, test_set_id)

    print(f'result: {result}\n')
    return result


def run_algo(lines: list[str], id: int) -> int:
    print(f'test set {id}')

    # vertical
    transposed = [''.join(s) for s in zip(*lines)]

    for i in range(1, len(transposed) - 1):
        found = False
        up = i
        down = i + 1
        while up >= 0 and down < len(transposed):
            if transposed[up] == transposed[down]:
                found = True
                up -= 1
                down += 1
            else:
                found = False
                break

        if found:
            result = (i + 1)
            print(f'found! column {i} -> {result}')
            return result

    # horizontal
    for i in range(1, len(lines) - 1):
        found = False
        up = i
        down = i + 1
        while up >= 0 and down < len(lines):
            if lines[up] == lines[down]:
                found = True
                up -= 1
                down += 1
            else:
                found = False
                break

        if found:
            result = (i + 1) * 100
            print(f'found! row {i} -> {result}')
            return result

    print('     not great')
    return 0


def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 13
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    # assert 405 == algo_part_one(test_input_file)
    algo_part_one(input_file)

    # 15564 - That's not the right answer; your answer is too low
    # 32866  - That's not the right answer; your answer is too low

    # part 2
    # assert 42 == algo_part_two(test_input_file)
    # assert 42 == algo_part_two(input_file)
