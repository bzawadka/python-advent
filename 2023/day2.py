import re

from common import read_file_to_list


# The Elf would first like to know which games would have been possible
# if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
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
            sum_val += (index + 1)

    return sum_val


# what is the fewest number of cubes of each color that
# could have been in the bag to make the game possible
def algo_part_two(input_file_name) -> int:
    print("running algo part two..." + input_file_name)

    lines = read_file_to_list(input_file_name)

    sum_val = 0
    for line in lines:
        game = line[8:]

        game_min_col = {'red': -1, 'green': -1, 'blue': -1}

        rounds = game.split(';')
        for r in rounds:
            pairs = re.findall(r'\d+\s\w+', r)
            for p in pairs:
                (amount, color) = str(p).split(' ')
                if int(amount) > game_min_col.get(color):
                    game_min_col[color] = int(amount)

        # The power of a set of cubes is equal to the numbers
        # of red, green, and blue cubes multiplied together
        power = game_min_col.get('red') * game_min_col.get('green') * game_min_col.get('blue')
        sum_val += power

    return sum_val


if __name__ == '__main__':
    day = 2
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 8 == algo_part_one(test_input_file)
    print(f'result: {algo_part_one(input_file)}')
    assert 2085 == algo_part_one(input_file)

    # part 2
    assert 2286 == algo_part_two(test_input_file)
    print(f'result: {algo_part_two(input_file)}')
    assert 79315 == algo_part_two(input_file)
