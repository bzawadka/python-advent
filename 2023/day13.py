import re

from common import read_file_to_list


# --- Day 13: Point of Incidence ---
# You note down the patterns of ash (.) and rocks (#) that you see
# as you walk (your puzzle input); perhaps by carefully analyzing these patterns,
# you can figure out where the mirrors are
def algo_part_one(input_file_name: str) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)

    for line in lines:
        print(line)

    result = 42
    print(f'result: {result}')
    return result


def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 13
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 405 == algo_part_one(test_input_file)
    # assert 42 == algo_part_one(input_file)

    # part 2
    # assert 42 == algo_part_two(test_input_file)
    # assert 42 == algo_part_two(input_file)
