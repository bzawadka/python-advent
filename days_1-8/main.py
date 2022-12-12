def day1_part2():
    file = open("input.txt")
    lines = file.readlines()
    print(f'there are {len(lines)} lines in the input file')

    elf_count = 0
    max_calories_so_far = {
        "min": 0,
        "med": 0,
        "max": 0
    }
    calories_for_current_elf = 0
    for line in lines:
        if line.strip():
            single_meal_calories = int(line.strip())
            calories_for_current_elf = calories_for_current_elf + single_meal_calories

            print(f"calories: {single_meal_calories}")
        else:
            print(f"elf {elf_count} has {calories_for_current_elf} calories in the backpack")
            if greater_than_any(calories_for_current_elf, max_calories_so_far):
                max_calories_so_far = reassign(calories_for_current_elf, max_calories_so_far)
            calories_for_current_elf = 0
            elf_count += 1

    total = max_calories_so_far.get("min") + max_calories_so_far.get("med") + max_calories_so_far.get("max")
    print(f"max calories of 3 elves: {total}")
    file.close()


def greater_than_any(current, others):
    if current > others.get("min"):
        return True
    if current > others.get("med"):
        return True
    if current > others.get("max"):
        return True
    return False


# example: max calories so far: 300 400 500
def reassign(current, max_calories_so_far):
    # current 600
    if current > max_calories_so_far.get("max"):
        new_dict = {
            "min": max_calories_so_far.get("med"),
            "med": max_calories_so_far.get("max"),
            "max": current
        }
        # 400 500 600
        return new_dict
    # current 450
    if current > max_calories_so_far.get("med"):
        new_dict = {
            "min": max_calories_so_far.get("med"),
            "med": current,
            "max": max_calories_so_far.get("max")
        }
        # 400 450 500
        return new_dict
    # current 350, expected: 350 400 500
    if current > max_calories_so_far.get("min"):
        new_dict = {
            "min": current,
            "med": max_calories_so_far.get("med"),
            "max": max_calories_so_far.get("max")
        }
        return new_dict
    return max_calories_so_far


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
    day1_part2()
