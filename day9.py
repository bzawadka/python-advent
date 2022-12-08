def algo() -> int:
    print("hello, day 9: ")

    lines_raw = open("day9_input.txt").readlines()
    lines = [line.strip() for line in lines_raw]
    print(lines)

    cosik = [i*2 for i in range(10)]
    print(cosik)

    cos = [[0] * 10 for _ in range(10)]
    print(cos)

    result = 0
    return result


if __name__ == '__main__':
    print(f'result: {algo()}')
