import re

from common import read_file_to_list


# --- Day 8: Haunted Wasteland ---
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


# What if the map isn't for people - what if the map is for ghosts
# the number of nodes with names ending in A is equal to the number ending in Z
# If you were a ghost, you'd probably just start at every node that ends with
# A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z
def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    lines = read_file_to_list(input_file_name)

    # read network map/dict
    network_left = {}
    network_right = {}
    network_starting_nodes = []
    for idx, line in enumerate(lines[2:]):
        (key, left, right) = re.findall(r'\w+', line)
        network_left[key] = left
        network_right[key] = right
        if key[2] == 'A':
            network_starting_nodes.append(key)

    print(f'there are special nodes {network_starting_nodes}')

    # navigate using directions
    directions = lines[0]
    current_nodes = network_starting_nodes

    steps = 0
    while not all_current_nodes_end_with_z(current_nodes):
        for d in directions:
            steps += 1
            match d:
                case 'L':
                    tmp = []
                    for cn in current_nodes:
                        cn = network_left[cn]
                        tmp.append(cn)
                    current_nodes = tmp
                    # print(f'L -> {current_nodes}')
                case 'R':
                    tmp = []
                    for cn in current_nodes:
                        cn = network_right[cn]
                        tmp.append(cn)
                    current_nodes = tmp
                    # print(f'R -> {current_nodes}')

            if all_current_nodes_end_with_z(current_nodes):
                break

    result = steps
    print(f'result: {result}')
    return result


def all_current_nodes_end_with_z(nodes) -> bool:
    for n in nodes:
        if n[2] != 'Z':
            return False
    return True


if __name__ == '__main__':
    day = 8
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    test_input_file2 = f'input/day{day}/testInput2.txt'
    input_file = f'input/day{day}/input.txt'
    test_input_file_part2 = f'input/day{day}/testInputPart2.txt'

    # assert 6 == algo_part_one(test_input_file)
    # assert 2 == algo_part_one(test_input_file2)
    # assert 19637 == algo_part_one(input_file)

    # part 2
    # assert 6 == algo_part_two(test_input_file_part2)
    algo_part_two(input_file)
    #     assert 42 ==
