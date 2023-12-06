import re


# --- Day 5: If You Give A Seed A Fertilizer ---
def algo_part_one(input_file_name: str) -> int:
    print("running algo part one..." + input_file_name)
    input_lines = open(input_file_name).readlines()
    seeds = [eval(i) for i in re.findall(r'\d+', input_lines[0])]
    maps = extract_maps(input_lines)

    for m in maps:
        for s_id, s in enumerate(seeds):
            for map_line in m:
                range_from = int(map_line[1])
                range_length = int(map_line[2])
                offset = int(map_line[0]) - range_from
                if seed_in_range(s, range_from, range_length):
                    seeds[s_id] = s + offset
                    break

    # the lowest location number that corresponds to any of the initial seeds
    result = min(seeds)
    print(f'result: {result}')
    return result


def seed_in_range(seed: int, range_from: int, length: int):
    return range_from <= seed <= range_from + length


def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    input_lines = open(input_file_name).readlines()
    seeds_with_ranges = [eval(i) for i in re.findall(r'\d+', input_lines[0])]
    seeds = seeds_with_ranges[0::2]
    ranges = seeds_with_ranges[1::2]
    maps = extract_maps(input_lines)

    min_location = 9999999999
    for seed_index, seed in enumerate(seeds):
        print(f'seed {seed} and its ancestors...')
        r = ranges[seed_index]
        for offset in range(0, r):
            actual_seed = seed + offset
            location = calculate_end_location_for_seed(maps, actual_seed)
            if location < min_location:
                min_location = location

    print(f'result: {min_location}')
    return min_location


def calculate_end_location_for_seed(maps, s: int):
    location = s
    for m in maps:
        for map_line in m:
            range_from = int(map_line[1])
            range_length = int(map_line[2])
            offset = int(map_line[0]) - range_from
            if seed_in_range(location, range_from, range_length):
                location = location + offset
                break

    if trace:
        print(f'seed {s} location {location}')
    return location


def extract_maps(input_lines: list):
    maps = [[], [], [], [], [], [], []]
    map_idx = -1
    for line in input_lines[1:]:
        if line.__contains__('map'):
            map_idx += 1
        else:
            numbers = re.findall(r'\d+', line)
            if numbers:
                maps[map_idx].append(numbers)
    return maps


if __name__ == '__main__':
    day = 5
    debug = True
    trace = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    # assert 35 == algo_part_one(test_input_file)
    # assert 3374647 == algo_part_one(input_file)

    # part 2
    # assert 46 == algo_part_two(test_input_file)
    algo_part_two(input_file)
