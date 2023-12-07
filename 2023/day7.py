from functools import cmp_to_key

from common import read_file_to_list


# --- Day 7: Camel Cards ---
# A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
# In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand
# If two hands have the same type, a second ordering rule takes effect
def algo_part_one(input_file_name: str) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)
    hands = [line.split(' ')[0] for line in lines]
    bids = [eval(line.split(' ')[1]) for line in lines]

    print(hands)
    sorted(hands, key=cmp_to_key(compare_hands))
    print(f'{hands} sorted')

    result = 42
    print(f'total winnings: {result}')
    return result


def compare_hands(left, right):
    if hand_type(left) < hand_type(right):
        return -1
    elif hand_type(left) > hand_type(right):
        return 1
    else:
        # If two hands have the same type, a second ordering rule takes effect.
        # Start by comparing the first card in each hand
        return 0


# Five of a kind    AAAAA   7
# Four of a kind    AA8AA   6
# Full house        23332   5
# Three of a kind   TTT98   4
# Two pair          23432   3
# One pair          A23A4   2
# High card         23456   1
def hand_type(hand: str) -> int:
    card_strengths = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8,
                      "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}

    if len(set(hand)) == 1:
        return 7

    return -1


def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 7
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    algo_part_one(test_input_file)
    # assert 6440 == algo_part_one(test_input_file)
    # assert 42 == algo_part_one(input_file)

    # part 2
    # assert 42 == algo_part_two(test_input_file)
    # assert 42 == algo_part_two(input_file)

# notes
#     my_data = [(4, 'B',), (3, 'A',), (2, 'C')]
#     sorted(my_data)
#     sorted(my_data, key=get_second)
#     sorted(my_data, key=lambda item: item[0])
# def get_second(item):
#     return item[1]
