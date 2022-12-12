from collections import deque


# The signal is a series of seemingly-random characters that the device receives one at a time.
# device that detects a start-of-packet marker in the datastream
# the start of a packet is indicated by a sequence of four characters that are all different
# your subroutine needs to identify the first position where the four most recently received
# characters were all different

def algo() -> int:
    print("hello, day 6: Tuning Trouble")

    data_buffer = open("day6_input.txt").read().strip()

    small_buffer = deque(maxlen=14)

    for idx, character in enumerate(data_buffer):
        small_buffer.append(character)

        # Check if all characters in the deque are different
        if len(set(small_buffer)) == 14:
            # starting sequence index
            return idx + 1

    return 0


if __name__ == '__main__':
    print(f'result: {algo()}')
    # 3534 is the expected result
