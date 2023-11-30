def algo() -> int:
    print("hello, day 12: Distress Signal")

    packets = read_instructions()

    for i in range(0, len(packets), 3):
        pair_l = packets[i]
        pair_r = packets[i + 1]
        print(f'compare {pair_l} to {pair_r}: {in_the_right_order(pair_l, pair_r)}')

    return -1


def in_the_right_order(pair_l: str, pair_r: str) -> bool:
    pair_l = pair_l.removeprefix('[').removesuffix(']')
    pair_r = pair_r.removeprefix('[').removesuffix(']')

    # Left side ran out of items, so inputs are in the right order
    if pair_l.strip() == '':
        return True

    # both values are integers
    items_l, items_r = pair_l.split(','), pair_r.split(',')
    first_l, first_r = items_l[0], items_r[0]
    if is_integer(first_l) and is_integer(first_r):
        if int(first_l) < int(first_r):
            return True
        elif int(first_l) > int(first_r):
            return False
        else:
            return in_the_right_order("just", "to compile")

    # plain lists - compare the items

    return False


def is_integer(smt: str) -> bool:
    return not smt.__contains__('[') and not smt.__contains__(']') and smt.isdigit()


def read_instructions() -> list[str]:
    instructions_raw = open(instruction_file).readlines()
    instructions_lines = [line.strip() for line in instructions_raw]
    return instructions_lines


if __name__ == '__main__':
    instruction_file = 'day13_input.txt'
    debug = False
    trace = False

    print(f'result: {algo()}')
