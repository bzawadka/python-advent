from collections import deque


# The signal is a series of seemingly-random characters that the device receives one at a time.
# device that detects a start-of-packet marker in the datastream
# the start of a packet is indicated by a sequence of four characters that are all different
# your subroutine needs to identify the first position where the four most recently received
# characters were all different

def algo() -> int:
    print("hello, day 6: Tuning Trouble")

    data_buffer = open("day6_input.txt").readlines().pop().strip()

    small_buffer = deque(maxlen=14)
    for idx, character in enumerate(data_buffer):
        small_buffer.append(character)
        print(f'buffer {small_buffer}')
        if all_characters_different(small_buffer):
            return idx + 1

    return 0


def all_characters_different(small_buffer: deque) -> bool:
    small_set = set(small_buffer)
    if len(small_set) == 14:
        return True
    return False


if __name__ == '__main__':
    print(f'result: {algo()}')
