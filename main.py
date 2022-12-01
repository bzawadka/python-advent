def day1_part1():
    file = open("input.txt")
    lines = file.readlines()
    print(f'there are {len(lines)} lines in the input file')

    elf_count = 0
    max_calories_so_far = 0
    calories_for_current_elf = 0
    for line in lines:
        if line.strip():
            single_meal_calories = int(line.strip())
            calories_for_current_elf = calories_for_current_elf + single_meal_calories

            print(f"calories: {single_meal_calories}")
        else:
            print(f"elf {elf_count} has {calories_for_current_elf} calories in the backpack")
            if calories_for_current_elf > max_calories_so_far:
                max_calories_so_far = calories_for_current_elf
            calories_for_current_elf = 0
            elf_count += 1

    print("max calories: {}".format(max_calories_so_far))
    file.close()


if __name__ == '__main__':
    day1_part1()
