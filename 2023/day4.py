import re

from common import read_file_to_list


# scratchcards
# each card has two lists of numbers separated by a vertical bar (|):
# a list of winning numbers and then a list of numbers you have.
# The first match makes the card worth one point and each match after the first doubles the point value of that card.
def algo_part_one(input_file_name) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)

    points_total = 0
    for line in lines:
        card_id_match = re.search(r'\d+', line)
        card_id_end_idx = card_id_match.end()
        card_id = line[card_id_match.start():card_id_end_idx]
        division_sign_idx = re.search(r'\|', line).start()

        winning_numbers = set(re.findall(r'\d+', line[card_id_end_idx:division_sign_idx]))
        my_numbers = re.findall(r'\d+', line[division_sign_idx:])

        numbers_won_counter = 0
        for n in my_numbers:
            if n in winning_numbers:
                numbers_won_counter += 1

        print(
            f'card {card_id} div at {division_sign_idx} winning {winning_numbers} mine {my_numbers} won {numbers_won_counter}')

        if numbers_won_counter:
            points_total += pow(2, numbers_won_counter - 1)

    return points_total


def algo_part_two(input_file_name) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 4
    debug = False
    trace = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 13 == algo_part_one(test_input_file)
    print(f'result: {algo_part_one(input_file)}')
    assert 20667 == algo_part_one(input_file)

    # part 2
    # assert 42 == algo_part_two(test_input_file)
    # print(f'result: {algo_part_two(input_file)}')
    # assert 42 == algo_part_two(input_file)
