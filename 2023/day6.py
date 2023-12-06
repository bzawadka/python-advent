import re

from common import read_file_to_list


# --- Day 6: Wait For It ---
# Determine the number of ways you could beat the record in each race
def algo_part_one(input_file_name: str) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)
    times = [eval(i) for i in re.findall(r'\d+', lines[0])]
    distances = [eval(i) for i in re.findall(r'\d+', lines[1])]
    races = {d: times[idx] for idx, d in enumerate(distances)}

    total_number_of_ways_to_win = 1
    for distance, time_limit in races.items():
        if debug:
            print(f'race distance {distance} time limit {time_limit}')
        total_number_of_ways_to_win *= calculate_number_of_times_to_win(time_limit, distance)

    # number of ways you can beat the record in each race
    print(f'result: {total_number_of_ways_to_win}')
    return total_number_of_ways_to_win


def calculate_number_of_times_to_win(time_limit: int, distance: int):
    ways_to_win_the_race = 0
    for t in range(1, time_limit):
        speed = t
        time_left = time_limit - t
        traveled_distance = speed * time_left
        if traveled_distance > distance:
            ways_to_win_the_race += 1

    if debug:
        print(f'ways to win: {ways_to_win_the_race}')
    return ways_to_win_the_race


def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    return algo_part_one(input_file_name)


if __name__ == '__main__':
    day = 6
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 288 == algo_part_one(test_input_file)
    assert 170000 == algo_part_one(input_file)

    # part 2
    # assert 42 == algo_part_two(test_input_file)
    # assert 42 == algo_part_two(input_file)
