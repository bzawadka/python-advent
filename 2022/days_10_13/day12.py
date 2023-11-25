import string
from collections import deque


def algo() -> int:
    heights = dict()
    start_point = (-1, -1)
    end_goal = (-1, -1)
    result = -1
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    print("hello, day 12: Hill Climbing Algorithm")

    # heightmap of the surrounding area
    # a is the lowest elevation, z is the highest elevation
    # current position (S) - elevation a
    # location that should get the best signal (E) - elevation z
    grid_list = read_instructions()
    height = len(grid_list)
    width = len(grid_list[0])

    for y, line in enumerate(grid_list):
        for x, char in enumerate(line):
            if char == "S":
                start_point = (x, y)
                heights[(x, y)] = 0
            elif char == "E":
                end_goal = (x, y)
                heights[(x, y)] = 25
            else:
                heights[(x, y)] = string.ascii_lowercase.index(char)

    visited = set()
    visited.add(start_point)

    q = deque()
    distance = 0
    q.appendleft((distance, start_point))

    while q:
        current_distance, current_location = q.popleft()
        if current_location == end_goal:
            result = current_distance
            break

        current_height = heights[current_location]
        x, y = current_location
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            # don't go outside the grid
            if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                continue

            neighbour_location = (new_x, new_y)
            if neighbour_location in visited:
                continue

            neighbour_height = heights[neighbour_location]
            if current_height + 1 >= neighbour_height:
                new_distance = current_distance + 1
                neighbour_entry = (new_distance, neighbour_location)
                q.append(neighbour_entry)
                visited.add(neighbour_location)

    return result


def read_instructions() -> list[str]:
    instructions_raw = open(instruction_file).readlines()
    instructions_lines = [line.strip() for line in instructions_raw]
    return instructions_lines


if __name__ == '__main__':
    instruction_file = 'day12_input.txt'
    debug = False
    trace = False

    print(f'result: {algo()}')
