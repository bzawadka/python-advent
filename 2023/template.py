import re

from common import read_file_to_list


def algo_part_one(input_file_name) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)

    for line in lines:
        print(line)

    return 42


def algo_part_two(input_file_name) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 1
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    print(f'result: {algo_part_one(test_input_file)}')
    assert 42 == algo_part_one(test_input_file)
    print(f'result: {algo_part_one(input_file)}')
    assert 42 == algo_part_one(input_file)

    # part 2
    assert 42 == algo_part_two(test_input_file)
    print(f'result: {algo_part_two(input_file)}')
    assert 42 == algo_part_two(input_file)
