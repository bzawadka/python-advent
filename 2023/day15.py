from enum import Enum

from common import read_file_to_list


# --- Day 15: Lens Library ---
def algo_part_one(input_file_name: str) -> int:
    print("running algo part one..." + input_file_name)
    lines = read_file_to_list(input_file_name)
    steps = [s for s in lines[0].split(",")]

    result = 0
    for step in steps:
        result += compute_hash_code_of(step)

    print(f'result: {result}')
    return result


# The HASH algorithm is a way to turn any string of characters into a single number in the range 0 to 255.
def compute_hash_code_of(s: str) -> int:
    value = 0
    for c in s:
        asc = ord(c)
        value += asc
        value *= 17
        value = value % 256
    return value


# The book goes on to describe
# a series of 256 boxes numbered 0 through 255
# lenses are organized by focal length ranging from 1 through 9
def algo_part_two(input_file_name: str) -> int:
    print("running algo part two..." + input_file_name)
    lines = read_file_to_list(input_file_name)
    steps = [s for s in lines[0].split(",")]
    boxes = [([], []) for _ in range(256)]  # labels and focal_lengths

    for step in steps:
        operation, label, focal_length = to_operation(step)
        box_id = compute_hash_code_of(label)

        labels, focal_lengths = boxes[box_id]
        label_idx = labels.index(label) if label in labels else -1
        match operation:
            case Operation.REMOVE:
                if label in labels:
                    focal_lengths.pop(label_idx)
                    labels.pop(label_idx)
            case Operation.ADD_OR_REPLACE:
                if label in labels:
                    # REPLACE
                    focal_lengths[label_idx] = focal_length
                else:
                    # ADD
                    labels.append(label)
                    focal_lengths.append(focal_length)

    # add up the focusing power of all the lenses
    result = 0
    for box_idx, box in enumerate(boxes):
        _, lengths = box
        if len(lengths) > 0:
            for slot_id, focal_length in enumerate(lengths):
                r = (box_idx + 1) * (slot_id + 1) * focal_length
                result += r

    print(f'result: {result}')


class Operation(Enum):
    ADD_OR_REPLACE = 1
    REMOVE = 2


def to_operation(step: str) -> (Operation, str, int):
    if step.find("=") != -1:
        label, value = step.split("=")
        return Operation.ADD_OR_REPLACE, label, int(value)
    if step.find("-") != -1:
        return Operation.REMOVE, step.split("-")[0], -1
    raise Exception("Sorry, should not happen")


if __name__ == '__main__':
    day = 15
    debug = False
    test_input_file = f'input/day{day}/testInput.txt'
    input_file = f'input/day{day}/input.txt'

    assert 1320 == algo_part_one(test_input_file)
    assert 515210 == algo_part_one(input_file)

    # part 2
    algo_part_two(test_input_file)  # 145
    algo_part_two(input_file)  # 246762
