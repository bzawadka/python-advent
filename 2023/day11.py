import itertools

import numpy as np

from common import read_file_to_list


def coordinate_key(x: int, y: int):
    return str(x) + '_' + str(y)


def from_coordinate_key(c_key: str) -> (int, int):
    x, y = c_key.split('_')
    return int(x), int(y)


# --- Day 11: Cosmic Expansion ---
# The researcher has collected a bunch of data and compiled the data into a single
# giant image (your puzzle input). The image includes empty space (.) and galaxies (#).
# The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies
# any rows or columns that contain no galaxies should all actually be twice as big
# Expand the universe,
# then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
def algo_part_one(input_file_name: str, size) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)

    # parse universe
    universe = np.zeros((size, size))
    galaxies = []
    for idx, line in enumerate(lines):
        for idy, c in enumerate(line):
            if c == '#':
                galaxies.append(coordinate_key(idx, idy))
                universe[idx, idy] = '1'
    print(f'galaxies: {galaxies}')

    # expand universe
    rows_with_no_galaxies = []
    for idx, row in enumerate(universe):
        if sum(row) == 0:
            rows_with_no_galaxies.append(idx)
    print(f'expand rows at: {rows_with_no_galaxies}')

    cols_with_no_galaxies = []
    for idx, row in enumerate(universe.transpose()):
        if sum(row) == 0:
            cols_with_no_galaxies.append(idx)
    print(f'expand cols at: {cols_with_no_galaxies}')

    expanded_universe = universe
    for row in rows_with_no_galaxies[::-1]:
        expanded_universe = np.insert(expanded_universe, row, 0, axis=0)

    for col in cols_with_no_galaxies[::-1]:
        expanded_universe = np.insert(expanded_universe, col, 0, axis=1)

    # expand galaxies
    galaxies = []
    for idx, line in enumerate(expanded_universe):
        for idy, c in enumerate(line):
            if c == 1:
                galaxies.append(coordinate_key(idx, idy))

    # CALCULATE DISTANCES
    sum_of_distances_between_galaxies = 0

    for pair in itertools.combinations(galaxies, 2):
        a, b = pair
        distance = calculate_distance_between(a, b)
        sum_of_distances_between_galaxies += distance

    # the sum of the shortest path between all 36 pairs of galaxies
    print(f'result: {sum_of_distances_between_galaxies}')
    return sum_of_distances_between_galaxies


def calculate_distance_between(a: str, b: str):
    ax, ay = from_coordinate_key(a)
    bx, by = from_coordinate_key(b)
    distance = abs(bx - ax) + abs(by - ay)
    return distance


def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 11
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 374 == algo_part_one(test_input_file, 10)
    assert 9686930 == algo_part_one(input_file, 140)

    # part 2
    # assert 42 == algo_part_two(test_input_file)
    # assert 42 == algo_part_two(input_file)
