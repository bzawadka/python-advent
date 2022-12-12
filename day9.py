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


previous_head_direction = 'undefined'
head_direction = 'undefined'
head_changed_direction = False


def calculate_how_many_positions_tail_visited(instructions) -> int:
    # positions of head and tail
    grid_size = 150
    head_x = 75
    head_y = 75
    tail_x = 75
    tail_y = 75
    positions_tail_visited_set = set()

    visualize_position(head_x, head_y, 'H', tail_x, tail_y, 'T', grid_size)
    mark_current_tail_position_as_visited(tail_x, tail_y, positions_tail_visited_set)

    for instr in instructions:
        print(f' == {instr.cmd} {instr.step} ========================')
        match instr.cmd:
            case 'R':
                for i in range(0, instr.step):
                    head_x += 1
                    update_head_direction_to('horizontal')

                    # in the first move
                    if i == 0:
                        # if head and tail were on the same position
                        if head_y == tail_y and head_x - 1 == tail_x:
                            print()  # do nothing
                        # if head and tail were on diagonal after previous move
                        elif tail_x + 2 == head_x:
                            tail_x += 1
                            if tail_y + 1 == head_y:
                                tail_y += 1
                            if head_y + 1 == tail_y:
                                tail_y -= 1
                        # if head and tail were next to each other, but...
                        elif head_changed_direction:
                            print()  # do nothing
                        # if head just got closer to the tail - from diagonal to adjacent
                        elif head_x == tail_x:
                            print()  # do nothing
                        else:
                            # tail was already behind the head, direction stays - tail shall continue
                            tail_x += 1
                    # in the second move
                    elif i == 1 or i == 2:
                        # if head and tail are touching diagonally
                        if tail_x + 1 == head_x:
                            print()  # do nothing
                        else:
                            if not head_changed_direction:
                                tail_x += 1
                            else:
                                # go right potentially diagonally - up or down
                                tail_x += 1
                                # print('if head is below tail, go right bottom with the tail')
                                if head_y < tail_y:
                                    tail_y -= 1
                                elif head_y > tail_y:
                                    tail_y += 1
                    else:
                        tail_x += 1
                    mark_current_tail_position_as_visited(tail_x, tail_y, positions_tail_visited_set)
                    if trace:
                        visualize_position(head_x, head_y, 'H', tail_x, tail_y, 'T', grid_size)

            case 'L':
                for i in range(0, instr.step):
                    head_x -= 1
                    update_head_direction_to('horizontal')

                    # in the first move
                    if i == 0:
                        # if head and tail were on the same position
                        if head_y == tail_y and head_x + 1 == tail_x:
                            print('')  # do nothing
                        # if head and tail were on diagonal after previous move
                        elif head_x + 2 == tail_x:
                            tail_x -= 1
                            if tail_y + 1 == head_y:
                                tail_y += 1
                            if head_y + 1 == tail_x:
                                tail_y -= 1
                        # if head and tail were next to each other, but...
                        elif head_changed_direction:
                            print()  # do nothing
                        # if head just got closer to the tail - from diagonal to adjacent
                        elif head_x == tail_x:
                            print()  # do nothing
                        else:
                            # tail was already behind the head, direction stays - tail shall continue
                            tail_x -= 1
                    # in the second move
                    elif i == 1 or i == 2:
                        if head_x + 1 == tail_x:
                            print()  # do nothing
                        else:
                            if not head_changed_direction:
                                tail_x -= 1
                            else:
                                # go left potentially diagonally - up or down
                                tail_x -= 1
                                # print('if head is below tail, go left bottom with the tail')
                                if head_y < tail_y:
                                    tail_y -= 1
                                elif head_y > tail_y:
                                    tail_y += 1
                    else:
                        tail_x -= 1

                    mark_current_tail_position_as_visited(tail_x, tail_y, positions_tail_visited_set)
                    if trace:
                        visualize_position(head_x, head_y, 'H', tail_x, tail_y, 'T', grid_size)

            case 'U':
                for i in range(0, instr.step):
                    head_y += 1
                    update_head_direction_to('vertical')

                    # in the first move
                    if i == 0:
                        # if head and tail were on the same position
                        if head_y - 1 == tail_y and head_x == tail_x:
                            print()  # do nothing
                        # if head and tail were on diagonal after previous move
                        elif tail_y + 2 == head_y:
                            tail_y += 1
                            if tail_x + 1 == head_x:
                                tail_x += 1
                            if head_x + 1 == tail_x:
                                tail_x -= 1
                        elif head_changed_direction:
                            print()  # do nothing
                        # if head just got closer to the tail - from diagonal to adjacent
                        elif head_y == tail_y:
                            print()  # do nothing
                        else:
                            # tail was already behind the head, direction stays - tail shall continue
                            tail_y += 1
                    # in the second move
                    elif i == 1 or i == 2:
                        if head_y - 1 == tail_y:
                            print()  # do nothing
                        else:
                            if not head_changed_direction:
                                tail_y += 1
                            else:
                                # go up diagonally - right or left
                                tail_y += 1
                                # print('if head is left from tail, go up left with the tail')
                                if head_x < tail_x:
                                    tail_x -= 1
                                elif head_x > tail_x:
                                    tail_x += 1
                    else:
                        tail_y += 1

                    mark_current_tail_position_as_visited(tail_x, tail_y, positions_tail_visited_set)
                    if trace:
                        visualize_position(head_x, head_y, 'H', tail_x, tail_y, 'T', grid_size)

            case 'D':
                for i in range(0, instr.step):
                    head_y -= 1
                    update_head_direction_to('vertical')

                    # in the first move
                    if i == 0:
                        # if head and tail were on the same position
                        if head_y + 1 == tail_y and head_x == tail_x:
                            print()  # do nothing
                        # if head and tail were on diagonal after previous move
                        elif head_y + 2 == tail_y:
                            tail_y -= 1
                            if tail_x + 1 == head_x:
                                tail_x += 1
                            if head_x + 1 == tail_x:
                                tail_x -= 1
                        elif head_changed_direction:  # POTENTIAL PROBLEM!!
                            print()  # do nothing
                        # if head just got closer to the tail - from diagonal to adjacent
                        elif head_y == tail_y:
                            print()  # do nothing
                        else:
                            # tail was already behind the head, direction stays - tail shall continue
                            tail_y -= 1
                    # in the second move
                    elif i == 1 or i == 2:
                        if head_y + 1 == tail_y:
                            print()  # do nothing
                        else:
                            if not head_changed_direction:
                                tail_y -= 1
                            else:
                                # go down diagonally - right or left
                                tail_y -= 1
                                if head_x > tail_x:
                                    tail_x += 1
                                elif head_x < tail_x:
                                    tail_x -= 1
                    else:
                        tail_y -= 1

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


def update_head_direction_to(direction: str):
    global previous_head_direction
    global head_direction
    global head_changed_direction

    previous_head_direction = head_direction
    head_direction = direction
    if previous_head_direction != 'undefined' and head_direction != previous_head_direction:
        head_changed_direction = True
        # print(f'what a twist of direction from {previous_head_direction} to {direction}!')


def mark_current_tail_position_as_visited(tail_x, tail_y, positions_tail_visited_set):
    item = str.format('{}{}', tail_x, tail_y)
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
    # 6374 - that's not the right answer
    # 6377 That's not the right answer
    # 6355, 6356 - your answer is too low.
    # 6321 - your answer is too low
