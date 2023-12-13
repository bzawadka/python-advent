from common import read_file_to_list


# --- Day 13: Point of Incidence ---
# You note down the patterns of ash (.) and rocks (#) that you see
# as you walk (your puzzle input); perhaps by carefully analyzing these patterns,
# you can figure out where the mirrors are
def algo_part_one(input_file_name: str) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)

    result = 0
    test_set = []
    test_set_id = 1
    for line in lines:
        if line.strip() != '':
            test_set.append(line)
        else:
            result += run_algo(test_set, test_set_id)
            test_set = []
            test_set_id += 1
    result += run_algo(test_set, test_set_id)

    print(f'result: {result}\n')
    return result


def run_algo(lines: list[str], test_set_id: int) -> int:
    # horizontal
    r = find_mirror_in(lines)
    if r > 0:
        return r * 100

    # vertical
    transposed = [''.join(s) for s in zip(*lines)]

    r = find_mirror_in(transposed)
    if r > 0:
        return r

    print('     not great')
    return 0


def find_mirror_in(lines: list[str]) -> int:
    for i in range(0, len(lines) - 1):
        found = False
        mirror_used = False
        up = i
        down = i + 1
        while up >= 0 and down < len(lines):
            if lines[up] == lines[down]:
                found = True
                up -= 1
                down += 1
            elif not mirror_used and differ_by_one_sign(lines[up], lines[down]):
                found = True
                up -= 1
                down += 1
                mirror_used = True
            else:
                found = False
                break

        if found:
            number_of_lines_before_the_mirror = (i + 1)
            print(f'found {number_of_lines_before_the_mirror}')
            return number_of_lines_before_the_mirror

    return 0


def differ_by_one_sign(s1: str, s2: str) -> bool:
    diff_cnt = 0
    for i, c in enumerate(s1):
        if c != s2[i]:
            diff_cnt += 1
        if diff_cnt > 1:
            return False

    diff_by_one = diff_cnt == 1
    if diff_by_one:
        print(f'     diff by one: {s1} {s2}')
    return diff_by_one


# You resume walking through the valley of mirrors and - SMACK! - run directly into one.
# every mirror has exactly one smudge: exactly one . or # should be the opposite type
def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 13
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    # lines = ["alane", "lapcu", "kotaf"]
    # transposed = [''.join(s) for s in zip(*lines)]
    #
    # print(transposed)
    # assert 405 == algo_part_one(test_input_file)
    # assert 33780 == algo_part_one(input_file)

    # part 2
    assert 400 == algo_part_two(test_input_file)
    algo_part_two(input_file)

    # 33913 That's not the right answer; your answer is too high
    # 33846 (guess)- That's not the right answer; your answer is too high
    # 33813 - That's not the right answer.
    # 33814 - That's not the right answer
    # 33812 - That's not the right answer
# 33815
# 33816
