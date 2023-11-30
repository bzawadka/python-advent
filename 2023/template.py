def algo(input_file_name) -> int:
    print("running algo...")

    lines = read_file_to_list(input_file_name)

    for line in lines:
        print(line)

    return 42


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
    assert 42 == algo(test_input_file)

    # run with non-test file, and print the result
    print(f'result: {algo(input_file)}')
