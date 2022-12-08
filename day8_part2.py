# What is the highest scenic score possible for any tree?
def algo() -> int:
    print("hello, day 8: Treetop Tree House")

    lines = open("day8_input.txt").readlines()
    grid = [line.strip() for line in lines]

    max_scenic_score = 0
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if (y == 0) or (x == 0) or (y == len(grid) - 1) or (x == len(lines) - 1):
                max_scenic_score = max_scenic_score
            else:
                curr_tree_height = int(grid[y][x])

                if debug:
                    print(f'analyzing [{y}][{x}]:{curr_tree_height}')

                # what's the viewing distance on the left?
                distance_left = 0
                for k in range(x - 1, -1, -1):
                    distance_left += 1
                    # print(f' comparing curr {curr_tree} to left {int(row[k])}')
                    if int(row[k]) >= curr_tree_height:
                        # print('not visible')
                        break

                # # what's the viewing distance on the right?
                distance_right = 0
                for k in range(x + 1, len(row)):
                    distance_right += 1
                    if int(row[k]) >= curr_tree_height:
                        break

                # # what's the viewing distance on the top?
                distance_top = 0
                for k in range(y - 1, -1, -1):
                    distance_top += 1
                    if int(grid[k][x]) >= curr_tree_height:
                        break

                # # what's the viewing distance on the bottom?
                distance_bottom = 0
                for k in range(y + 1, len(grid)):
                    distance_bottom += 1
                    if int(grid[k][x]) >= curr_tree_height:
                        break

                if debug:
                    print(f'distance_left is {distance_left}')
                    print(f'distance_right is {distance_right}')
                    print(f'distance_top is {distance_top}')
                    print(f'distance_bottom is {distance_bottom}')

                scenic_score = distance_right * distance_left * distance_top * distance_bottom

                if debug:
                    print(f'scenic score of [{y}][{x}]:{grid[y][x]} is...: {scenic_score}\n---')

                if scenic_score > max_scenic_score:
                    max_scenic_score = scenic_score

    return max_scenic_score


if __name__ == '__main__':
    debug = False
    print(f'result: {algo()}')
    # 479400 sis the right answer
