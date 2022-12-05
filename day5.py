from collections import deque


def algo():
    print("hello, day 5: Supply Stacks")

    instructions = open("day5_test_input.txt").readlines()[5:]
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

        print(f'move {how_many} from {move_from} to {move_to}')

        for idx in range(how_many):
            item = stacks[move_from].pop()
            stacks[move_to].append(item)

    print(f'result is: {stacks[0]}, {stacks[1]}, {stacks[2]}')

    print(f'on the top we have {stacks[0].pop()}{stacks[1].pop()}{stacks[2].pop()}')


def manually_create_input() -> list[deque]:
    stack_1 = deque()
    stack_1.append('Z')
    stack_1.append('N')

    stack_2 = deque()
    stack_2.append('M')
    stack_2.append('C')
    stack_2.append('D')

    stack_3 = deque()
    stack_3.append('P')

    return [stack_1, stack_2, stack_3]


if __name__ == '__main__':
    algo()
