# Every section has a unique ID number
# , and each Elf is assigned a range of section IDs.
def algo():
    print("hello, day 4: Camp Cleanup")

    pairs = open("day4_input.txt").readlines()
    print(f'there are {len(pairs)} pairs')

    range_overlap_counter = 0
    for pair in pairs:
        first_range_raw, second_range_raw = pair.strip().split(",")
        first_range = first_range_raw.split("-")
        second_range = second_range_raw.split("-")
        print(f'comparing {first_range} to {second_range}')
        if one_range_contained_in_another(list(map(int, first_range)), list(map(int, second_range))):
            range_overlap_counter += 1

    print(f'result is: {range_overlap_counter}')


# ranges, like 2-8,3-7
def one_range_contained_in_another(A: list[int], B: list[int]) -> bool:
    if A[1] < B[0] or A[0] > B[1]:
        return False

    if A[0] <= B[0]:
        if B[1] <= A[1]:
            print(f'bingo!')
            return True
    if A[0] >= B[0]:
        if B[1] >= A[1]:
            print(f'bingo!')
            return True
    return False


if __name__ == '__main__':
    algo()
