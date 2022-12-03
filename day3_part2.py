import string
from typing import AnyStr, List


def day3():
    print("hello, day 3: Rucksacks")

    all_rucksacks = open("day3_test_input.txt").readlines()
    print(f'there are {len(all_rucksacks)} rucksacks')

    elf_number = 0
    sum_of_the_priorities = 0
    for idx, single_rucksack in enumerate(all_rucksacks):
        if (idx * 3) > len(all_rucksacks):
            break

        rucksack_items = [*all_rucksacks[idx * 3].strip()]
        second_rucksack = all_rucksacks[idx * 3 + 1].strip()
        third_rucksack = all_rucksacks[idx * 3 + 2].strip()

        repeated_item = find_item_repeated_in_all_rucksacks(elf_number, rucksack_items, second_rucksack, third_rucksack)
        item_priority_value = calculate_priority(repeated_item)
        print(f'duplicated item found {repeated_item} in all 3 rucksacks with value {item_priority_value}')
        sum_of_the_priorities = sum_of_the_priorities + item_priority_value

        elf_number += 1

    print(f'my total score is: {sum_of_the_priorities}')


def find_item_repeated_in_all_rucksacks(elf_number: int, rucksack_items: List[AnyStr], second_rucksack: string,
                                        third_rucksack: string) -> string:
    repeated_item = 'undefined'

    #
    #         # a group
    #         first_rucksack_characters           /// idx * 3
    #         second_rucksack_string              /// idx * 3 + 1
    #         third_rucksack_string               /// idx * 3 + 2
    #             going through each character in the 1st single_rucksack
    #                 if 2nd contains it and 3rd contains it
    #                     break/return

    return repeated_item


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
