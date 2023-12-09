from enum import Enum

from common import read_file_to_list


# --- Day 9: Mirage Maintenance ---
# The OASIS produces a report of many values and how they are changing over time (your puzzle input).
# Each line in the report contains the history of a single value
# your environmental report should include a prediction of the next value in each history
def algo_part_one(input_file_name: str) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)
    result = 0

    for line in lines:
        # Phase 1: calculate last number in each sub-sequence: 0, 1, 5, 15
        last_numbers = find_numbers_for(line, WhichNumber.LAST)

        # Phase 2: calculate new numbers: 0, 1, 7, 28
        # 1   3   6  10  15  21  28
        #   2   3   4   5   6   7
        #     1   1   1   1   1
        #       0   0   0   0
        new_numbers = [0]
        for idx, n in enumerate(reversed(last_numbers)):
            if idx == 0:
                continue
            new_n = n + new_numbers[idx - 1]
            new_numbers.append(new_n)

        # Phase 3: add 28 to the result
        last_one = new_numbers.pop()
        result += last_one

    # What is the sum of extrapolated values?
    print(f'result: {result}')
    return result


class WhichNumber(Enum):
    FIRST = 1
    LAST = 2


def find_numbers_for(line: str, first_or_last: WhichNumber) -> list[int]:
    # 1 3 6 10 15 21
    numbers = []
    # Phase 1: calculate last number in each sub-sequence: 0, 1, 5, 15
    # 1   3   6  10  15  21
    #   2   3   4   5   6
    #     1   1   1   1
    #       0   0   0
    current_line = line
    while not all_chars_are_zeros_in(current_line):
        current_l = current_line.split(' ')
        match first_or_last:
            case WhichNumber.FIRST:
                first_number = int(current_l[0])
                numbers.append(first_number)
            case WhichNumber.LAST:
                last_number = int(current_l[-1])
                numbers.append(last_number)

        tmp_line = ''
        for idx, num in enumerate(current_l):
            if idx == len(current_l) - 1:
                break
            n = int(current_l[idx + 1]) - int(num)
            if tmp_line != '':
                tmp_line += ' '
            tmp_line += str(n)

        current_line = tmp_line

    numbers.append(0)
    return numbers


def all_chars_are_zeros_in(s: str) -> bool:
    if len(set(s)) == 2 and ('0' in set(s) and ' ' in set(s)):
        return True
    return False


def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    lines = read_file_to_list(input_file_name)

    result = 0
    for line in lines:
        first_numbers = find_numbers_for(line, WhichNumber.FIRST)

        new_numbers = [0]
        for idx, n in enumerate(reversed(first_numbers)):
            if idx == 0:
                continue
            new_n = n - new_numbers[idx - 1]
            new_numbers.append(new_n)

        result += new_numbers.pop()

    # What is the sum of extrapolated values?
    print(f'result: {result}')
    return result


if __name__ == '__main__':
    day = 9
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 114 == algo_part_one(test_input_file)
    assert 1581679977 == algo_part_one(input_file)

    # part 2
    assert 2 == algo_part_two(test_input_file)
    assert 889 == algo_part_two(input_file)
