import re

from common import read_file_to_list


# --- Day 15: Lens Library ---
def algo_part_one(input_file_name: str) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)
    steps = [s for s in lines[0].split(",")]

    result = 0
    for line in steps:
        result += compute_hash_value_of(line)

    print(f'result: {result}')
    return result


def compute_hash_value_of(s: str) -> int:
    value = 0
    for c in s:
        asc = ord(c)
        value += asc
        value *= 17
        value = value % 256
    return value


def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 15
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 1320 == algo_part_one(test_input_file)
    algo_part_one(input_file)

    # part 2
    # assert 42 == algo_part_two(test_input_file)
    # assert 42 == algo_part_two(input_file)
