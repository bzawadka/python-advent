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
        seed_already_updated = [False for _ in range(0, len(seeds))]
        for s_id, s in enumerate(seeds):
            if seed_already_updated[s_id]:
                break

            for map_line in m:
                range_from = int(map_line[1])
                range_length = int(map_line[2])
                offset = int(map_line[0]) - range_from
                if seed_in_range(int(s), range_from, range_length):
                    seeds[s_id] = int(s) + offset
                    seed_already_updated[s_id] = True

    # the lowest location number that corresponds to any of the initial seeds
    result = min(seeds)
    print(f'result: {result}')
    return result


def seed_in_range(seed: int, range_from: int, length: int):
    return range_from <= seed <= range_from + length


def algo_part_two(input_file_name) -> int:
    print("running algo part two..." + input_file_name)
    lines_raw = open(input_file_name).readlines()
    seeds_with_ranges = re.findall(r'\d+', lines_raw[0])
    seeds = seeds_with_ranges[0::2]
    ranges = seeds_with_ranges[1::2]

    actual_unique_seeds = set()
    for s_idx, s in enumerate(seeds):
        r = int(ranges[s_idx])
        for i in range(0, r):
            actual_seed = int(s) + i
            actual_unique_seeds.add(actual_seed)

    actual_seeds = list(actual_unique_seeds)
    print(f'number of actual seeds: {len(actual_seeds)}')

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

    min_location = 9999999999
    for s in actual_seeds:
        location = calculate_end_location_for_seed(maps, s)
        if location < min_location:
            min_location = location

    print(f'result: {min_location}')
    return min_location


def calculate_end_location_for_seed(maps, s):
    location = s
    for m in maps:
        for map_line in m:
            range_from = int(map_line[1])
            range_length = int(map_line[2])
            offset = int(map_line[0]) - range_from
            if seed_in_range(location, range_from, range_length):
                location = location + offset
                break

    if debug:
        print(f'seed {s} location {location}')
    return location


if __name__ == '__main__':
    day = 5
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    # assert 35 == algo_part_one(test_input_file)
    # assert 3374647 == algo_part_one(input_file)

    # part 2
    assert 46 == algo_part_two(test_input_file)
    # algo_part_two(input_file)
