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
        if is_there_an_overlap(list(map(int, first_range)), list(map(int, second_range))):
            range_overlap_counter += 1

    print(f'result is: {range_overlap_counter}')
    #  787  That's not the right answer; your answer is too low
    #  946 - too high


def is_there_an_overlap(A: list[int], B: list[int]) -> bool:
    if A[1] < B[0] or A[0] > B[1]:
        return False

    if A[0] <= B[0]:
        if B[1] <= A[1]:
            print('bingo!')
            return True

    if A[0] >= B[0]:
        if B[1] >= A[1]:
            print('bingo!')
            return True

    if A[1] >= B[0]:
        if B[0] >= A[0]:
            print('overlap!')
            return True

    if A[0] >= B[0] and A[1] <= B[1]:
        print('overlap!')
        return True

    if B[0] >= A[0] and B[1] <= A[1]:
        print('overlap!')
        return True

    if A[0] == B[0] or A[0] == B[1] or A[1] == B[0] or A[1] == B[1]:
        print('overlap!')
        return True

    if B[1] >= A[0]:
        print('new overlap!')
        return True

    return False


# ranges, like 2-8,3-7
def one_range_contained_in_another(A: list[int], B: list[int]) -> bool:
    if A[1] < B[0] or A[0] > B[1]:
        return False

    if A[0] <= B[0]:
        if B[1] <= A[1]:
            print('bingo!')
            return True
    if A[0] >= B[0]:
        if B[1] >= A[1]:
            print('bingo!')
            return True
    return False


if __name__ == '__main__':
    algo()
