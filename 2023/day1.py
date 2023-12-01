import re

def algo_part_one(input_file_name) -> int:
    print("running algo..." + input_file_name)

    lines = read_file_to_list(input_file_name)

    sum_val = 0
    for line in lines:
        first_d = -1
        last_d = -1
        number = 0
        for c in line:
            if c.isdigit():
                if first_d == -1:
                    first_d = c
                else:
                    last_d = c

        if last_d == -1:
            last_d = first_d

        number = int(first_d) * 10 + int(last_d)

        print(number)
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

    # run with test file and expect given result
    assert 281 == algo(test_input_file)

    # run with non-test file": 1, "and print the result
    print(f'result: {algo(input_file)}')
