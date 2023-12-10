from enum import Enum

from common import read_file_to_list


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


# --- Day 10: Pipe Maze ---
# Find the single giant loop starting at S
# How many steps along the loop does it take to get
# from the starting position to the point farthest from the starting position?
def algo_part_one(input_file_name: str, s_x: int, s_y: int,
                  direction_a: Direction, direction_b: Direction) -> int:
    print("running algo part one..." + input_file_name)
    the_map = read_file_to_list(input_file_name)

    print(f'starting at: {the_map[s_x][s_y]}')
    ax = s_x
    ay = s_y
    bx = s_x
    by = s_y
    distance = 0
    while distance < 1000000:
        distance += 1
        # make the move - both A and B
        # result is new coordinates and new direction
        # check if A and B are met,
        #   if so: stop the loop
        (ax, ay, direction_a) = make_the_move(ax, ay, direction_a, the_map)
        (bx, by, direction_b) = make_the_move(bx, by, direction_b, the_map)
        if ax == bx and ay == by:
            break

    print(f'result: {distance}')
    return distance


def make_the_move(x: int, y: int, direction: Direction, the_map: list[str]) -> (int, int, Direction):
    match direction:
        case Direction.NORTH:
            x -= 1
        case Direction.EAST:
            y += 1
        case Direction.SOUTH:
            x += 1
        case Direction.WEST:
            y -= 1

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


def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 10
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 8 == algo_part_one(test_input_file, 2, 0, Direction.EAST, Direction.SOUTH)
    algo_part_one(input_file, 96, 101, Direction.EAST, Direction.NORTH)

    # part 2
    # assert 42 == algo_part_two(test_input_file)
    # assert 42 == algo_part_two(input_file)
