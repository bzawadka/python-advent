import re
from math import lcm

from common import read_file_to_list


# --- Day 8: Haunted Wasteland ---
def algo_part_one(input_file_name: str) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)

    # read network map/dict
    directions_left = {}
    directions_right = {}
    for idx, line in enumerate(lines[2:]):
        (key, left, right) = re.findall(r'\w+', line)
        directions_left[key] = left
        directions_right[key] = right

    # navigate using directions
    instructions = lines[0]

    steps = 0
    current_node = 'AAA'
    while current_node != 'ZZZ':
        for i in instructions:
            steps += 1
            match i:
                case 'L':
                    current_node = directions_left[current_node]
                case 'R':
                    current_node = directions_right[current_node]
            if current_node == 'ZZZ':
                break

    print(f'result: {steps}')
    return steps


# What if the map isn't for people - what if the map is for ghosts
# the number of nodes with names ending in A is equal to the number ending in Z
# If you were a ghost, you'd probably just start at every node that ends with
# A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z
def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    lines = read_file_to_list(input_file_name)

    # read network map/dict
    directions_left = {}
    directions_right = {}
    network_starting_nodes = []
    for idx, line in enumerate(lines[2:]):
        (k, left, right) = re.findall(r'\w+', line)
        key = str(k)
        directions_left[key] = str(left)
        directions_right[key] = str(right)
        if key.endswith('A'):
            network_starting_nodes.append(key)

    print(f'network starting nodes: {network_starting_nodes}')

    # navigate using directions
    instructions = lines[0]

    steps = 0
    results = {}
    current_nodes = network_starting_nodes
    while len(results) != len(network_starting_nodes):
        for i in instructions:
            steps += 1
            match i:
                case 'L':
                    tmp = []
                    for cn in current_nodes:
                        cn = directions_left[cn]
                        tmp.append(cn)
                        if cn.endswith('Z'):
                            results[cn] = steps
                    current_nodes = tmp
                case 'R':
                    tmp = []
                    for cn in current_nodes:
                        cn = directions_right[cn]
                        tmp.append(cn)
                        if cn.endswith('Z'):
                            results[cn] = steps
                    current_nodes = tmp

            if len(results.keys()) == len(network_starting_nodes):
                break

    print(f'network ending nodes, with the distance: {results}')
    distances = [v for v in results.values()]
    far_away_distance_where_they_will_meet = lcm(*distances)
    print(f'result: {far_away_distance_where_they_will_meet}')
    return far_away_distance_where_they_will_meet


if __name__ == '__main__':
    day = 8
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    test_input_file2 = f'input/day{day}/testInput2.txt'
    input_file = f'input/day{day}/input.txt'
    test_input_file_part2 = f'input/day{day}/testInputPart2.txt'

    assert 6 == algo_part_one(test_input_file)
    assert 2 == algo_part_one(test_input_file2)
    assert 19637 == algo_part_one(input_file)

    # part 2
    assert 6 == algo_part_two(test_input_file_part2)
    assert 8811050362409 == algo_part_two(input_file)
