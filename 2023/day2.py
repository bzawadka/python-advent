# The Elf would first like to know which games would have been possible
# if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
import re


def algo_part_one(input_file_name) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)

    rules = {'red': 12, 'green': 13, 'blue': 14}

    sum_val = 0
    for index, line in enumerate(lines):
        game = line[8:]
        game_possible = True

        rounds = game.split(';')
        for r in rounds:
            round_possible = True
            # check if the round is possible if not break the loop
            pairs = re.findall(r'\d+\s\w+', r)
            for p in pairs:
                (amount, color) = str(p).split(' ')
                if int(amount) > rules.get(color):
                    round_possible = False
                    break
            if not round_possible:
                game_possible = False
                break

        if game_possible:
            print(f'game {index + 1} is possible')
            sum_val += (index + 1)

    print(f'sum is {sum_val}')
    return sum_val


def algo_part_two(input_file_name) -> int:
    print("running algo part two..." + input_file_name)

    lines = read_file_to_list(input_file_name)

    sum_val = 0
    # for line in lines:

    return sum_val


def read_file_to_list(file) -> list[str]:
    instructions_raw = open(file).readlines()
    instructions_lines = [line.strip() for line in instructions_raw]
    return instructions_lines


if __name__ == '__main__':
    day = 2
    debug = False
    trace = False
    test_input_file = f'input/day{day}/testInput.txt'
    test_input_file_p1 = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 8 == algo_part_one(test_input_file_p1)
    print(f'result: {algo_part_one(input_file)}')
    assert 2085 == algo_part_one(input_file)

    # part 2
    # assert 281 == algo_part_two(test_input_file)
    # assert 55291 == algo_part_two(input_file)
