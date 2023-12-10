from enum import Enum

from common import read_file_to_list


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


def coordinate_key(x: int, y: int):
    return str(x) + '_' + str(y)


# --- Day 10: Pipe Maze ---
# Find the single giant loop starting at S
# How many steps along the loop does it take to get
# from the starting position to the point farthest from the starting position?
def algo_part_one(input_file_name: str, start_x: int, start_y: int,
                  direction_a: Direction, direction_b: Direction) -> int:
    print("running algo part one..." + input_file_name)
    the_map = read_file_to_list(input_file_name)

    print(f'starting at: {the_map[start_x][start_y]}')
    ax = start_x
    ay = start_y
    bx = start_x
    by = start_y
    loop_coordinates = set()
    loop_coordinates.add(coordinate_key(start_x, start_y))
    distance = 0
    while True:
        distance += 1
        # make the move - both A and B; result is new coordinates and new direction
        # check if A and B met, if so: stop the loop
        (ax, ay, direction_a) = make_the_move(ax, ay, direction_a, the_map, loop_coordinates)
        (bx, by, direction_b) = make_the_move(bx, by, direction_b, the_map, loop_coordinates)
        if ax == bx and ay == by:
            break

    print(f'result: {distance}')
    return distance


def make_the_move(x: int, y: int, direction: Direction, the_map: list[str], loop_coordinates) -> (
        int, int, Direction):
    match direction:
        case Direction.NORTH:
            x -= 1
        case Direction.EAST:
            y += 1
        case Direction.SOUTH:
            x += 1
        case Direction.WEST:
            y -= 1

    loop_coordinates.add(coordinate_key(x, y))

    next_map_piece = the_map[x][y]
    match next_map_piece:
        case 'J':
            direction = Direction.NORTH if direction == Direction.EAST else Direction.WEST
        case 'F':
            direction = Direction.EAST if direction == Direction.NORTH else Direction.SOUTH
        case '7':
            direction = Direction.SOUTH if direction == Direction.EAST else Direction.WEST
        case 'L':
            direction = Direction.EAST if direction == Direction.SOUTH else Direction.NORTH
        case '-':
            direction = direction
        case '|':
            direction = direction
            # unchanged, it must have been north or south already
            # direction = Direction.NORTH if direction == Direction.NORTH else Direction.SOUTH
        case _:
            print(f'unknown direction: {next_map_piece}')

    return x, y, direction


def algo_part_two(input_file_name: str, start_x: int, start_y: int,
                  direction_a: Direction, direction_b: Direction) -> int:
    print("running algo part two..." + input_file_name)
    the_map = read_file_to_list(input_file_name)

    print(f'starting at: {the_map[start_x][start_y]}')
    ax = start_x
    ay = start_y
    bx = start_x
    by = start_y

    loop_coordinates = set()
    loop_coordinates.add(coordinate_key(start_x, start_y))

    # discover the loop with coordinates
    while True:
        # make the move - both A and B
        # result is new coordinates and new direction
        # check if A and B are met,
        #   if so: stop the loop
        (ax, ay, direction_a) = make_the_move(ax, ay, direction_a, the_map, loop_coordinates)
        (bx, by, direction_b) = make_the_move(bx, by, direction_b, the_map, loop_coordinates)

        if ax == bx and ay == by:
            break

    # clean the map, remove random pipes that are not part of the loop
    clean_map = []
    for x, line in enumerate(the_map):
        clean_row = ''
        for y, c in enumerate(line):
            clean_row += c if coordinate_key(x, y) in loop_coordinates else '.'
        clean_map.append(clean_row)

    no_tiles_inside_the_loop = 0
    # for each coordinate
    #   if not part of the loop
    #       count I J L S to the left of it
    #           if odd number -> must be in the loop
    for x, line in enumerate(clean_map):
        for y, c in enumerate(line):
            if coordinate_key(x, y) not in loop_coordinates:
                count = count_special_chars_in(line[:y])
                if count & 1:
                    no_tiles_inside_the_loop += 1

    print(f'result: {no_tiles_inside_the_loop}')
    return no_tiles_inside_the_loop


def count_special_chars_in(line: str) -> int:
    return line.count('|') + line.count('J') + line.count('L') + line.count('S')


if __name__ == '__main__':
    day = 10
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    test_input_file_2 = f'input/day{day}/testInput2.txt'
    test_input_file_3 = f'input/day{day}/testInput3.txt'
    input_file = f'input/day{day}/input.txt'

    assert 8 == algo_part_one(test_input_file, 2, 0, Direction.EAST, Direction.SOUTH)
    assert 6890 == algo_part_one(input_file, 96, 101, Direction.EAST, Direction.NORTH)

    # part 2
    # #NB Check your input, if 'S' behaves like "|", "J", "L", then leave
    # # 'S' in array, otherwise remove it
    assert 8 == algo_part_two(test_input_file_2, 4, 12, Direction.EAST, Direction.SOUTH)
    assert 10 == algo_part_two(test_input_file_3, 0, 4, Direction.WEST, Direction.SOUTH)
    assert 453 == algo_part_two(input_file, 96, 101, Direction.EAST, Direction.NORTH)
