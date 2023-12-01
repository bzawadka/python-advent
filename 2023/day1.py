import re


def algo_part_one(input_file_name) -> int:
    print("running algo..." + input_file_name)

    lines = read_file_to_list(input_file_name)

    sum_val = 0
    for line in lines:
        first_d = find_first_digit(line)
        last_d = find_first_digit(line[::-1])
        number = int(first_d) * 10 + int(last_d)
        sum_val += number

    return sum_val


def find_first_digit(line):
    for c in line:
        if c.isdigit():
            return int(c)


def find_first_digit_or_str(line):
    for idx, c in enumerate(line):
        if c.isdigit():
            return int(c)
        else:
            if line[idx:].startswith('one'):
                return 1
            if line[idx:].startswith('two'):
                return 2
            if line[idx:].startswith('three'):
                return 3
            if line[idx:].startswith('four'):
                return 4
            if line[idx:].startswith('five'):
                return 5
            if line[idx:].startswith('six'):
                return 6
            if line[idx:].startswith('seven'):
                return 7
            if line[idx:].startswith('eight'):
                return 8
            if line[idx:].startswith('nine'):
                return 9


def find_first_digit_or_str_reversed(line):
    for idx, c in enumerate(line):
        if c.isdigit():
            return int(c)
        else:
            if line[idx:].startswith('one'[::-1]):
                return 1
            if line[idx:].startswith('two'[::-1]):
                return 2
            if line[idx:].startswith('three'[::-1]):
                return 3
            if line[idx:].startswith('four'[::-1]):
                return 4
            if line[idx:].startswith('five'[::-1]):
                return 5
            if line[idx:].startswith('six'[::-1]):
                return 6
            if line[idx:].startswith('seven'[::-1]):
                return 7
            if line[idx:].startswith('eight'[::-1]):
                return 8
            if line[idx:].startswith('nine'[::-1]):
                return 9


def algo_part_two(input_file_name) -> int:
    print("running algo..." + input_file_name)

    lines = read_file_to_list(input_file_name)

    sum_val = 0
    for line in lines:
        first_d = find_first_digit_or_str(line)
        last_d = find_first_digit_or_str_reversed(line[::-1])
        number = int(first_d) * 10 + int(last_d)
        sum_val += number

    return sum_val


def algo(input_file_name) -> int:
    print("running algo..." + input_file_name)

    lines = read_file_to_list(input_file_name)

    sum_val = 0
    for line in lines:

        line = line.replace("nine", "9")
        line = line.replace("eight", "8")
        line = line.replace("three", "3")
        line = line.replace("two", "2")
        line = line.replace("one", "1")
        line = line.replace("four", "4")
        line = line.replace("five", "5")
        line = line.replace("six", "6")
        line = line.replace("seven", "7")

        print(line)

        # find all digits with their positions
        # digits = re.findall(r'\d', line)
        first_d = -1
        first_d_idx = -1
        last_d = -1
        last_d_idx = -1
        for idx, c in enumerate(line):
            if c.isdigit():
                if first_d == -1:
                    first_d = c
                    first_d_idx = idx
                else:
                    last_d = c
                    last_d_idx = idx

        if last_d == -1:
            last_d = first_d
            last_d_idx = first_d_idx

        # print(f'{first_d} at {first_d_idx} and {last_d} with {last_d_idx}')
        print(f'{first_d}{last_d}')

        # find all words with their positions

        number = int(first_d) * 10 + int(last_d)

        sum_val += number

    return sum_val


def read_file_to_list(file) -> list[str]:
    instructions_raw = open(file).readlines()
    instructions_lines = [line.strip() for line in instructions_raw]
    return instructions_lines


if __name__ == '__main__':
    day = 1
    debug = False
    trace = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 1 == find_first_digit_or_str('abcone2threexyz')
    assert 4 == find_first_digit_or_str('4nineeightseven2')
    assert 2 == find_first_digit_or_str('xtwone3four')

    assert 3 == find_first_digit_or_str_reversed('abcone2threexyz'[::-1])
    assert 2 == find_first_digit_or_str_reversed('4nineeightseven2'[::-1])
    assert 6 == find_first_digit_or_str_reversed('7pqrstsixteen'[::-1])

    # run with test file and expect given result
    assert 281 == algo_part_two(test_input_file)

    # run with non-test file": 1, "and print the result
    print(f'result: {algo_part_two(input_file)}')