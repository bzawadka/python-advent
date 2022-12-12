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
    instructions_raw = open(instruction_file).readlines()
    instructions_lines = [line.strip() for line in instructions_raw]
    instructions = [Instr(it.split(" ")[0], int(it.split(" ")[1])) for it in instructions_lines]
    return instructions


def calculate_how_many_positions_tail_visited(instructions) -> int:
    # positions of head and tail
    grid_size = 150
    start_x = 75
    start_y = 75
    head_x = start_x
    head_y = start_y
    tail_x = start_x
    tail_y = start_y
    positions_tail_visited_set = set()

    mark_current_tail_position_as_visited(tail_x, tail_y, positions_tail_visited_set)

    for instr in instructions:
        if trace:
            print(f' == {instr.cmd} {instr.step} ===')
        match instr.cmd:
            case 'R':
                for i in range(0, instr.step):
                    previous_head_x = head_x
                    head_x += 1

                    if tail_x + 1 == previous_head_x:
                        # tail moves along
                        tail_x += 1
                        # tail moves diagonally
                        if tail_y + 1 == head_y:
                            tail_y += 1
                        if tail_y - 1 == head_y:
                            tail_y -= 1
                    # otherwise don't move tail

                    mark_current_tail_position_as_visited(tail_x, tail_y, positions_tail_visited_set)
                    if trace:
                        visualize_position(head_x, head_y, 'H', tail_x, tail_y, 'T', grid_size)

            case 'L':
                for i in range(0, instr.step):
                    previous_head_x = head_x
                    head_x -= 1

                    if tail_x - 1 == previous_head_x:
                        # tail moves along
                        tail_x -= 1
                        # tail moves diagonally
                        if tail_y + 1 == head_y:
                            tail_y += 1
                        if tail_y - 1 == head_y:
                            tail_y -= 1
                    # otherwise don't move tail

                    mark_current_tail_position_as_visited(tail_x, tail_y, positions_tail_visited_set)
                    if trace:
                        visualize_position(head_x, head_y, 'H', tail_x, tail_y, 'T', grid_size)

            case 'U':
                for i in range(0, instr.step):
                    previous_head_y = head_y
                    head_y += 1

                    if tail_y + 1 == previous_head_y:
                        # tail moves along
                        tail_y += 1
                        # tail moves diagonally
                        if tail_x + 1 == head_x:
                            tail_x += 1
                        if tail_x - 1 == head_x:
                            tail_x -= 1
                    # otherwise don't move tail

                    mark_current_tail_position_as_visited(tail_x, tail_y, positions_tail_visited_set)
                    if trace:
                        visualize_position(head_x, head_y, 'H', tail_x, tail_y, 'T', grid_size)

            case 'D':
                for i in range(0, instr.step):
                    previous_head_y = head_y
                    head_y -= 1

                    if tail_y - 1 == previous_head_y:
                        # tail moves along
                        tail_y -= 1
                        # tail moves diagonally
                        if tail_x + 1 == head_x:
                            tail_x += 1
                        if tail_x - 1 == head_x:
                            tail_x -= 1

                    mark_current_tail_position_as_visited(tail_x, tail_y, positions_tail_visited_set)
                    if trace:
                        visualize_position(head_x, head_y, 'H', tail_x, tail_y, 'T', grid_size)
            case _:
                raise SyntaxError

        if debug:
            visualize_position(head_x, head_y, 'H', tail_x, tail_y, 'T', grid_size)

        if head_x < 0 or head_y < 0 or tail_x < 0 or tail_y < 0:
            raise IndexError(f'head[{head_x}][{head_y}] vs tail[{tail_x}][{tail_y}]')

    if debug:
        print(f'positions tail visited: {positions_tail_visited_set}')

    return len(positions_tail_visited_set)


def mark_current_tail_position_as_visited(tail_x, tail_y, positions_tail_visited_set):
    item = str.format('{}_{}', tail_x, tail_y)
    positions_tail_visited_set.add(item)


def visualize_position(x: int, y: int, first_icon: str, a: int, b: int, second_icon: str, grid_size):
    grid = [[0] * grid_size for _ in range(grid_size)]
    # bottom left corner is [0][0]
    grid[grid_size - 1 - y][x] = first_icon
    grid[grid_size - 1 - b][a] = second_icon
    if x == a and y == b:
        grid[grid_size - 1 - y][x] = first_icon + second_icon

    # print('y')
    # print('^')
    for line in grid:
        print(f'| {line}')
    print('o---------------------> x')
    print()


if __name__ == '__main__':
    instruction_file = 'day9_input.txt'
    debug = False
    trace = False

    # How many positions does the tail of the rope visit at least once?
    print(f'result: {algo()}')
    # 6428 your answer is too high

    # 6376 - That's the right answer!

    # 6374 - that's not the right answer
    # 6377 That's not the right answer
    # 6355, 6356 - your answer is too low.
    # 6321 - your answer is too low
