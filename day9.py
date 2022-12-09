from dataclasses import dataclass


@dataclass
class Instr:
    cmd: str
    step: int


def algo() -> int:
    print("hello, day 9: Rope Bridge")
    instructions = read_instructions()
    result = calculate_how_many_positions_tail_visited(instructions)
    return result


def read_instructions() -> list[Instr]:
    instructions_raw = open("day9_test_input.txt").readlines()
    instructions_lines = [line.strip() for line in instructions_raw]
    instructions = [Instr(it.split(" ")[0], int(it.split(" ")[1])) for it in instructions_lines]
    if debug:
        print(instructions)
    return instructions


def calculate_how_many_positions_tail_visited(instructions) -> int:
    # positions of head and tail
    head_x = 0
    head_y = 0

    positions_tail_visited_set = set()
    positions_tail_visited_set.add(current_tail_position_as_str())

    for instr in instructions:
        match instr.cmd:
            case 'R':
                for i in range(0, instr.step):
                    head_x += 1
            case 'L':
                for i in range(0, instr.step):
                    head_x -= 1
            case 'U':
                for i in range(0, instr.step):
                    head_y += 1
            case 'D':
                for i in range(0, instr.step):
                    head_y -= 1
            case _:
                raise SyntaxError

        if debug:
            print(f'head is [{head_x}][{head_y}]')
            visualize_position(head_x, head_y, 'H')

    if debug:
        print(f'positions tail visited: {positions_tail_visited_set}')
    return len(positions_tail_visited_set)


def current_tail_position_as_str():
    return str.format('{}{}', tail_x, tail_y)


def visualize_position(x: int, y: int, character: str):
    grid = [[0] * grid_size for _ in range(grid_size)]
    # bottom left corner is [0][0]
    grid[grid_size - 1 - y][x] = character
    print('y')
    print('^')
    for line in grid:
        print(f'| {line}')
    print('o---------------------> x')
    print()


if __name__ == '__main__':
    debug = True
    grid_size = 6
    tail_x = 0
    tail_y = 0
    # How many positions does the tail of the rope visit at least once?
    print(f'result: {algo()}')
