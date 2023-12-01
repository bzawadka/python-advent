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

    char_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

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
    assert 142 == algo(test_input_file)

    # run with non-test file": 1, "and print the result
    print(f'result: {algo(input_file)}')
