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

        if numbers_won_counter:
            points_total += pow(2, numbers_won_counter - 1)

    return points_total


# There's no such thing as "points". Instead, scratchcards only cause you to win more scratchcards
# equal to the number of winning numbers you have.
# how many total scratchcards do you end up with?
def algo_part_two(input_file_name) -> int:
    print("running algo part two..." + input_file_name)
    lines = read_file_to_list(input_file_name)

    cards_counter = {(i + 1): 1 for i in range(len(lines))}

    for line in lines:
        card_id_match = re.search(r'\d+', line)
        card_id_end_idx = card_id_match.end()
        card_id = int(line[card_id_match.start():card_id_end_idx])

        division_sign_idx = re.search(r'\|', line).start()
        other_numbers = set(re.findall(r'\d+', line[card_id_end_idx:division_sign_idx]))
        my_numbers = re.findall(r'\d+', line[division_sign_idx:])

        matching_numbers_counter = 0
        for n in my_numbers:
            if n in other_numbers:
                matching_numbers_counter += 1

        card_ids_to_add = set()
        if matching_numbers_counter:
            card_ids_to_add = [i for i in range(card_id + 1, card_id + matching_numbers_counter + 1)]

        how_many_of_me_exist = cards_counter.get(card_id)
        number_of_copies_to_add = how_many_of_me_exist

        for c_id in card_ids_to_add:
            tmp = cards_counter.get(c_id)
            tmp += number_of_copies_to_add
            cards_counter[c_id] = tmp

        if debug:
            print(f'card {card_id} has {matching_numbers_counter} matches, so adding cards {card_ids_to_add}')

    cards_total = 0
    for key, value in cards_counter.items():
        cards_total += value

    return cards_total


if __name__ == '__main__':
    day = 4
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 13 == algo_part_one(test_input_file)
    print(f'result: {algo_part_one(input_file)}')
    assert 20667 == algo_part_one(input_file)

    # part 2
    print(f'result: {algo_part_two(test_input_file)}')
    assert 30 == algo_part_two(test_input_file)
    print(f'result: {algo_part_two(input_file)}')
    assert 5833065 == algo_part_two(input_file)
