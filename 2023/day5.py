import re


def algo_part_one(input_file_name) -> int:
    print("running algo part one..." + input_file_name)
    lines_raw = open(input_file_name).readlines()
    seeds = re.findall(r'\d+', lines_raw[0])

    # parse input
    maps = [[], [], [], [], [], [], []]
    map_idx = -1
    for line in lines_raw[1:]:
        if line.__contains__('map'):
            map_idx += 1
        else:
            numbers = re.findall(r'\d+', line)
            if numbers:
                maps[map_idx].append(numbers)

    for m in maps:
        print(m)
        seed_already_updated = [False for _ in range(0, len(seeds))]
        for s_id, s in enumerate(seeds):
            if seed_already_updated[s_id]:
                break

            for map_line in m:
                range_from = int(map_line[1])
                range_length = int(map_line[2])
                offset = int(map_line[0]) - range_from
                print(map_line)
                # if s in range(range_from, range_from + range_length):
                if seed_in_range(int(s), range_from, range_length):
                    print(f'seed {s} should be moved by {offset}')
                    # update seed
                    seeds[s_id] = int(s) + offset
                    seed_already_updated[s_id] = True

    # the lowest location number that corresponds to any of the initial seeds
    return min(seeds)


def seed_in_range(seed, range_from, length):
    return range_from <= seed <= range_from + length


def algo_part_two(input_file_name) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 5
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    print(f'result: {algo_part_one(test_input_file)}')
    assert 35 == algo_part_one(test_input_file)
    print(f'result: {algo_part_one(input_file)}')
    # assert 42 == algo_part_one(input_file)

    # part 2
    # assert 42 == algo_part_two(test_input_file)
    # print(f'result: {algo_part_two(input_file)}')
    # assert 42 == algo_part_two(input_file)
