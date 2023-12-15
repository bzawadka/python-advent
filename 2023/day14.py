import re

from common import read_file_to_list


# --- Day 14: Parabolic Reflector Dish ---
def algo_part_one(input_file_name: str) -> int:
    print("running algo part one..." + input_file_name)
    lines_raw = open(input_file_name).readlines()
    dish = [list(line.strip()) for line in lines_raw]

    # tilt north
    for idy, l in enumerate(dish):
        if idy == 0:
            continue

        if 'O' in l:
            for idx, c in enumerate(l):
                if c == 'O':
                    # try to move it as much north as possible
                    target_y = idy
                    for y in range(idy - 1, -1, -1):
                        if dish[y][idx] == '.':
                            target_y = y
                            continue
                        if dish[y][idx] == '#' or dish[y][idx] == 'O':
                            break
                    # move the rock
                    if idy != target_y:
                        dish[target_y][idx] = 'O'
                        dish[idy][idx] = '.'

    # The amount of load caused by a single rounded rock (O) is equal to the number of rows
    # from the rock to the south edge of the platform, including the row the rock is on
    result = 0
    for idy, l in enumerate(dish):
        r = (len(dish) - idy) * l.count('O')
        result += r

    # The total load is the sum of the load caused by all the rounded rocks
    print(f'result: {result}')
    return result


def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 14
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 136 == algo_part_one(test_input_file)
    assert 110090 == algo_part_one(input_file)

    # part 2
    # assert 42 == algo_part_two(test_input_file)
    # assert 42 == algo_part_two(input_file)
