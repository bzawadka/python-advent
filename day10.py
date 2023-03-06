from dataclasses import dataclass

# clock circuit, cycle, signal strength
from typing import Optional


@dataclass
class Instr:
    cmd: str
    value: int


def algo() -> int:
    print("Day 10: Cathode-Ray Tube")
    instructions = read_instructions_from_file('day10_input.txt')
    result = calculate_sum_of_signal_strengths(instructions)
    return result


def read_instructions_from_file(instruction_file: str) -> list[Instr]:
    lines = open(instruction_file).readlines()
    stripped_lines = [line.strip() for line in lines]
    instructions = [parse_instruction(line) for line in stripped_lines]
    return instructions


def parse_instruction(instr: str) -> Instr:
    if instr.__contains__("noop"):
        return Instr(instr, 0)
    else:
        return Instr(instr.split(" ")[0], int(instr.split(" ")[1]))


def calculate_sum_of_signal_strengths(instructions: list[Instr]) -> int:

    # instruction for execution in a cycle, where a key is CYCLE number
    scheduled_inst = dict()
    scheduled_inst[1] = instructions[0]

    cycle_no = 1
    register_val = 1

    sum_of_strength = 0

    while scheduled_inst:
        # read instruction
        if cycle_no < len(instructions):
            new_instr: Instr = instructions[cycle_no]
            if scheduled_inst:
                current_max_cycle = max(sorted(scheduled_inst))
            else:
                current_max_cycle = cycle_no + 1

            match new_instr.cmd:
                case 'noop':
                    scheduled_inst[current_max_cycle + 1] = new_instr
                case 'addx':
                    scheduled_inst[current_max_cycle + 2] = new_instr

        print(f'cycle: {cycle_no}, register: {register_val}')

        sum_of_strength += calculate_signal_strength(20, cycle_no, register_val)
        sum_of_strength += calculate_signal_strength(60, cycle_no, register_val)
        sum_of_strength += calculate_signal_strength(100, cycle_no, register_val)
        sum_of_strength += calculate_signal_strength(140, cycle_no, register_val)
        sum_of_strength += calculate_signal_strength(180, cycle_no, register_val)
        sum_of_strength += calculate_signal_strength(220, cycle_no, register_val)

        # execute instruction
        cycle_no_for_exec = min(sorted(scheduled_inst))
        if cycle_no == cycle_no_for_exec:
            instr: Instr = scheduled_inst[cycle_no_for_exec]
            register_val += instr.value
            print(f'I shall execute {instr} at the end of cycle {cycle_no}')
            del scheduled_inst[cycle_no_for_exec]

        print(f'cycle: {cycle_no}, register at the end of cycle: {register_val}')

        cycle_no += 1

    return sum_of_strength


def calculate_signal_strength(cycle, current_cycle, register_val):
    if cycle == current_cycle:
        signal_strength = current_cycle * register_val
        print(f'signal strength {cycle}th: {signal_strength}')
        return signal_strength
    else:
        return 0


if __name__ == '__main__':
    debug = False
    trace = False
    print(f'result: {algo()}')
    # part 1: 14520
