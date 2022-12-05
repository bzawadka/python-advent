from collections import deque


def algo():
    print("hello, day 5: Supply Stacks")

    instructions = open("day5_input.txt").readlines()[10:]
    print(f'there are {len(instructions)} instructions')

    stacks = manually_create_input()

    for line in instructions:
        instruction = line.strip()
        instruction_digits = [int(s) for s in str.split(instruction) if s.isdigit()]
        # alternative way
        # reg = [int(s) for s in re.findall('\\d+', instruction)]

        how_many = instruction_digits[0]
        move_from = instruction_digits[1] - 1
        move_to = instruction_digits[2] - 1

        print(f'move {how_many} from {move_from + 1} to {move_to + 1}')

        if how_many == 1:
            item = stacks[move_from].pop()
            stacks[move_to].append(item)
        if how_many > 1:
            # Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:
            print(f'do something else...')
            temp_stack = deque()
            for idx in range(how_many):
                item = stacks[move_from].pop()
                temp_stack.append(item)
            for idx in range(how_many):
                item = temp_stack.pop()
                stacks[move_to].append(item)

    for stack in stacks:
        print(f'result is: {stack}')

    result = ''
    for stack in stacks:
        result = result + stack.pop()

    print(f'on the top we have {result}')


def manually_create_input() -> list[deque]:
    #     [G] [R]                 [P]
    #     [H] [W]     [T] [P]     [H]
    #     [F] [T] [P] [B] [D]     [N]
    # [L] [T] [M] [Q] [L] [C]     [Z]
    # [C] [C] [N] [V] [S] [H]     [V] [G]
    # [G] [L] [F] [D] [M] [V] [T] [J] [H]
    # [M] [D] [J] [F] [F] [N] [C] [S] [F]
    # [Q] [R] [V] [J] [N] [R] [H] [G] [Z]
    #  1   2   3   4   5   6   7   8   9
    stack_9 = deque()
    stack_9.append('Z')
    stack_9.append('F')
    stack_9.append('H')
    stack_9.append('G')

    stack_8 = deque()
    stack_8.append('G')
    stack_8.append('S')
    stack_8.append('J')
    stack_8.append('V')
    stack_8.append('Z')
    stack_8.append('N')
    stack_8.append('H')
    stack_8.append('P')

    stack_7 = deque()
    stack_7.append('H')
    stack_7.append('C')
    stack_7.append('T')

    stack_6 = deque()
    stack_6.append('R')
    stack_6.append('N')
    stack_6.append('V')
    stack_6.append('H')
    stack_6.append('C')
    stack_6.append('D')
    stack_6.append('P')

    stack_5 = deque()
    stack_5.append('N')
    stack_5.append('F')
    stack_5.append('M')
    stack_5.append('S')
    stack_5.append('L')
    stack_5.append('B')
    stack_5.append('T')

    stack_4 = deque()
    stack_4.append('J')
    stack_4.append('F')
    stack_4.append('D')
    stack_4.append('V')
    stack_4.append('Q')
    stack_4.append('P')

    stack_1 = deque()
    stack_1.append('Q')
    stack_1.append('M')
    stack_1.append('G')
    stack_1.append('C')
    stack_1.append('L')

    stack_2 = deque()
    stack_2.append('R')
    stack_2.append('D')
    stack_2.append('L')
    stack_2.append('C')
    stack_2.append('T')
    stack_2.append('F')
    stack_2.append('H')
    stack_2.append('G')

    stack_3 = deque()
    stack_3.append('V')
    stack_3.append('J')
    stack_3.append('F')
    stack_3.append('N')
    stack_3.append('M')
    stack_3.append('T')
    stack_3.append('W')
    stack_3.append('R')

    return [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]


if __name__ == '__main__':
    algo()
