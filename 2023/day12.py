import re

from common import read_file_to_list


# --- Day 12: Hot Springs ---
# condition records of which springs are damaged - your puzzle input)
# the springs are arranged into rows
# the condition records show every spring and whether it is operational (.) or damaged (#).
# for some springs, it is simply unknown (?)
def algo_part_one(input_file_name: str) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)
    count = 0
    for line in lines:
        condition_record, groups = line.split(' ')
        no_groups = [eval(i) for i in re.findall(r'\d+', groups)]
        count += count_possible_arrangements(condition_record, no_groups)

    print(f'result: {count}')
    return count


# Add all the possible arrangement counts
def count_possible_arrangements(record: str, no_groups: list[int]):
    index = 0

    show_possible_arrangements(index, record)

    return -1


# ???.###
# len == 7
def show_possible_arrangements(index: int, record: str):
    if index == len(record):
        print(record)
        return

    match record[index]:
        case '.' | '#':
            show_possible_arrangements(index + 1, record)
        case '?':
            show_possible_arrangements(index + 1, record[:index] + '.' + record[index + 1:])
            show_possible_arrangements(index + 1, record[:index] + '#' + record[index + 1:])

    return


def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 12
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 21 == algo_part_one(test_input_file)
    # assert 42 == algo_part_one(input_file)

    # part 2
    # assert 42 == algo_part_two(test_input_file)
    # assert 42 == algo_part_two(input_file)
