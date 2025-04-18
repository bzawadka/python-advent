import re

from common import read_file_to_list


def algo_part_one(input_file_name: str, map_length: int) -> int:
    print("running algo part one..." + input_file_name)
    instructions = read_file_to_list(input_file_name)

    dig_map = ['.' * map_length for _ in range(map_length)]
    starting_point = map_length / 2, map_length / 2
    x = int(starting_point[0])
    y = int(starting_point[1])
    dig_map = dig(dig_map, x, y)

    for instr in instructions:
        direction = instr[0]
        length = int(re.search(r'\d+', instr).group(0))
        match direction:
            case 'R':
                for i in range(length):
                    x += 1
                    dig_map = dig(dig_map, x, y)
            case 'L':
                for i in range(length):
                    x -= 1
                    dig_map = dig(dig_map, x, y)
            case 'D':
                for i in range(length):
                    y += 1
                    dig_map = dig(dig_map, x, y)
            case 'U':
                for i in range(length):
                    y -= 1
                    dig_map = dig(dig_map, x, y)

    result = 0
    for row in dig_map:
        if '#' in row:
            match = re.findall(r'\\#', row)
            print(f'found {match.count()} # in row')
            # match.start()
            # match.end()

    print(f'result: {result}')
    return result


def dig(dig_map: list[str], x: int, y: int):
    s = dig_map[x]
    return s[:y] + '#' + s[y + 1:]


def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name, 50)


if __name__ == '__main__':
    day = 18
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 62 == algo_part_one(test_input_file, 50)
    # assert 42 == algo_part_one(input_file)

    # part 2
    # assert 42 == algo_part_two(test_input_file)
    # assert 42 == algo_part_two(input_file)
