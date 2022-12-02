def day2_part2():
    print("hello, day 2: Rock Paper Scissors tournament")

    strategy_guide = open("day2_input.txt")
    round_instructions = strategy_guide.readlines()
    print(f'there are {len(round_instructions)} lines in the strategy guide')

    total_score = 0
    for instruction in round_instructions:
        opponent_move, expected_outcome = instruction.split(" ", 1)
        expected_outcome = expected_outcome.strip()
        my_shape = choose_my_shape(opponent_move, expected_outcome)
        round_score = shape_score(my_shape) + did_i_win_score(opponent_move, my_shape)
        print(f'opponent_move is {opponent_move}, expected outcome is {expected_outcome}; round score is {round_score}')
        total_score = total_score + round_score
    print(f'my total score is: {total_score}')


def choose_my_shape(opponent_move, expected_outcome):
    match expected_outcome:
        case 'X':  # X means you need to lose
            match opponent_move:
                case 'A':  # Rock
                    return 'Z'  # X for Rock, Y for Paper, and Z for Scissors
                case 'B':  # Paper
                    return 'X'
                case 'C':  # Scissors
                    return 'Y'
        case 'Y':  # Y means you need to end the round in a draw
            match opponent_move:
                case 'A':  # Rock
                    return 'X'
                case 'B':  # Paper
                    return 'Y'
                case 'C':  # Scissors
                    return 'Z'
        case 'Z':  # Z means you need to win
            match opponent_move:
                case 'A':  # Rock
                    return 'Y'
                case 'B':  # Paper
                    return 'Z'
                case 'C':  # Scissors
                    return 'X'
        case _:
            raise ValueError('unexpected')


# the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# X for Rock, Y for Paper, and Z for Scissors
def shape_score(my_shape):
    match my_shape:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3
        case _:
            raise ValueError(f'Cannot determine shape score: "{my_shape}"')


# opponent_move: A for Rock, B for Paper, and C for Scissors
# my_move: X for Rock, Y for Paper, and Z for Scissors
# scoring: 0 if you lost, 3 if the round was a draw, and 6 if you won
def did_i_win_score(opponent_move, my_move):
    match opponent_move:
        case 'A':  # Rock
            match my_move:
                case 'X':  # Rock
                    return 3
                case 'Y':  # Paper
                    return 6
                case 'Z':  # Scissors
                    return 0
                case _:
                    raise ValueError('just in case')
        case 'B':  # Paper
            match my_move:
                case 'X':  # Rock
                    return 0
                case 'Y':  # Paper
                    return 3
                case 'Z':  # Scissors
                    return 6
                case _:
                    raise ValueError('just in case')
        case 'C':  # Scissors
            match my_move:
                case 'X':  # Rock
                    return 6
                case 'Y':  # Paper
                    return 0
                case 'Z':  # Scissors
                    return 3
                case _:
                    raise ValueError('just in case')
        case _:
            raise ValueError(f'Cannot determine game score: him: {opponent_move}, myself: {my_move}')


if __name__ == '__main__':
    day2_part2()
