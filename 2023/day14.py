# --- Day 14: Parabolic Reflector Dish ---
# The dish is made up of many small mirrors
def algo_part_one(input_file_name: str) -> int:
    print("running algo part one..." + input_file_name)
    lines_raw = open(input_file_name).readlines()
    dish = [list(line.strip()) for line in lines_raw]

    dish = tilt_north(dish)
    load = calculate_load(dish)

    print(f'result: {load}')
    return load


def tilt_north(dish: [[]]) -> [[]]:
    # going form top to bottom
    for idy in range(1, len(dish)):
        row = dish[idy]
        if ROCK in row:
            for idx in range(0, len(row)):
                if dish[idy][idx] == ROCK:
                    # try to move it as much north as possible
                    target_y = idy
                    for y in range(idy - 1, -1, -1):
                        if dish[y][idx] == EMPTY_SPACE:
                            target_y = y
                            continue
                        if dish[y][idx] == HARD_ROCK or dish[y][idx] == ROCK:
                            break
                    # move the rock
                    if idy != target_y:
                        dish[target_y][idx] = ROCK
                        dish[idy][idx] = EMPTY_SPACE
    return dish


def tilt_right(dish: [[]]) -> [[]]:
    # going form left to right
    for idy in range(0, len(dish)):
        row = dish[idy]
        if ROCK in row:
            for idx in range(len(row) - 1, -1, -1):
                if dish[idy][idx] == ROCK:
                    # try to move it as much right as possible
                    target_x = idx
                    for x in range(idx + 1, len(row)):
                        if dish[idy][x] == EMPTY_SPACE:
                            target_x = x
                            continue
                        if dish[idy][x] == HARD_ROCK or dish[idy][x] == ROCK:
                            break
                    # move the rock
                    if idx != target_x:
                        dish[idy][target_x] = ROCK
                        dish[idy][idx] = EMPTY_SPACE
    return dish


def tilt_south(dish: [[]]) -> [[]]:
    # going form bottom to top
    for idy in range(len(dish) - 1, -1, -1):
        row = dish[idy]
        if ROCK in row:
            for idx in range(0, len(row)):
                if dish[idy][idx] == ROCK:
                    target_y = idy
                    for y in range(idy + 1, len(dish)):
                        if dish[y][idx] == EMPTY_SPACE:
                            target_y = y
                            continue
                        if dish[y][idx] == HARD_ROCK or dish[y][idx] == ROCK:
                            break
                    if idy != target_y:
                        dish[target_y][idx] = ROCK
                        dish[idy][idx] = EMPTY_SPACE
    return dish


# The amount of load caused by a single rounded rock (O) is equal to the number of rows
# from the rock to the south edge of the platform, including the row the rock is on
def calculate_load(dish) -> int:
    total_load = 0
    for idy, l in enumerate(dish):
        load = (len(dish) - idy) * l.count(ROCK)
        total_load += load
    # The total load is the sum of the load caused by all the rounded rocks
    return total_load


def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)

    lines_raw = open(input_file_name).readlines()
    dish = [list(line.strip()) for line in lines_raw]

    dish = tilt_right(dish)

    print(dish[0])
    print(dish[1])
    print(dish[2])
    print(dish[3])
    print(dish[4])
    print(dish[5])
    print(dish[6])
    print(dish[7])
    print(dish[8])
    print(dish[9])

    return calculate_load(dish)


if __name__ == '__main__':
    day = 14
    ROCK = 'O'
    HARD_ROCK = '#'
    EMPTY_SPACE = '.'

    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    # assert 136 == algo_part_one(test_input_file)
    # assert 110090 == algo_part_one(input_file)

    # part 2
    algo_part_two(test_input_file)
    # assert 42 == algo_part_two(input_file)
