import string
from typing import AnyStr, List


def day3_part2():
    print("hello, day 3: Rucksacks")

    all_rucksacks = open("day3_input.txt").readlines()
    print(f'there are {len(all_rucksacks)} rucksacks')

    elf_number = 0
    sum_of_the_priorities = 0
    for idx, single_rucksack in enumerate(all_rucksacks):
        if (idx * 3) >= len(all_rucksacks):
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
    for rucksack_item in rucksack_items:
        if rucksack_item in second_rucksack and rucksack_item in third_rucksack:
            repeated_item = rucksack_item
            break
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
    day3_part2()
