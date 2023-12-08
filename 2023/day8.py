import re

from common import read_file_to_list


def algo_part_one(input_file_name: str) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)

    # read network map/dict
    network_left = {}
    network_right = {}
    network_starting_node = ""
    for idx, line in enumerate(lines[2:]):
        (key, left, right) = re.findall(r'\w+', line)
        network_left[key] = left
        network_right[key] = right
        if idx == 0:
            network_starting_node = key

    # navigate using directions
    directions = lines[0]
    current_node = 'AAA'

    steps = 0
    while current_node != 'ZZZ':
        for d in directions:
            steps += 1
            match d:
                case 'L':
                    current_node = network_left[current_node]
                case 'R':
                    current_node = network_right[current_node]
            if current_node == 'ZZZ':
                break

    result = steps
    print(f'result: {result}')
    return result


def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 8
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    test_input_file2 = f'input/day{day}/testInput2.txt'
    input_file = f'input/day{day}/input.txt'

    # assert 6 == algo_part_one(test_input_file)
    # assert 2 == algo_part_one(test_input_file2)
    # algo_part_one(input_file)
    assert 42 == algo_part_one(input_file)

    # part 2
    # assert 42 == algo_part_two(test_input_file)
    # assert 42 == algo_part_two(input_file)
