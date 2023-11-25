import string
from typing import AnyStr, List


def day3():
    print("hello, day 3: Rucksacks")

    packing_list = open("day3_input.txt").readlines()
    print(f'there are {len(packing_list)} rucksacks')

    elf_number = 0
    sum_of_the_priorities = 0
    for single_rucksack in packing_list:
        rucksack_items = [*single_rucksack.strip()]
        repeated_item = find_item_repeated_in_both_rucksack_compartments(elf_number, rucksack_items)
        item_priority_value = calculate_priority(repeated_item)
        print(f'duplicated item found {repeated_item} with value {item_priority_value}')
        sum_of_the_priorities = sum_of_the_priorities + item_priority_value
        elf_number += 1

    print(f'my total score is: {sum_of_the_priorities}')


# Find the item type that appears in both compartments of each rucksack
#   A given rucksack always has the same number of items in each of its two compartments
#   - the first half of the characters represent items in the first compartment, while
#   - the second half of the characters represent items in the second compartment
def find_item_repeated_in_both_rucksack_compartments(elf_number: int, rucksack_items: List[AnyStr]) -> string:
    compartment_size = int(len(rucksack_items) / 2)
    print(f'elf {elf_number} has items {rucksack_items} and compartments of size {compartment_size}')

    repeated_item = 'undefined'
    for idx, item_first_compartment in enumerate(rucksack_items):
        for item_second_compartment in rucksack_items[-compartment_size:]:
            if item_first_compartment == item_second_compartment:
                repeated_item = item_second_compartment
                break

        if repeated_item != 'undefined':
            break

        if idx > compartment_size:
            raise ValueError('we went too far in the rucksack - duplicate was not found')

    return repeated_item


# To help prioritize item rearrangement, every item type can be converted to a priority:
# - Lowercase item types a through z have priorities 1 through 26.
# - Uppercase item types A through Z have priorities 27 through 52.
def calculate_priority(character: AnyStr) -> int:
    if character.isupper():
        return ord(character) - 38
    if character.islower():
        return ord(character) - 96
    return -1000


if __name__ == '__main__':
    day3()
