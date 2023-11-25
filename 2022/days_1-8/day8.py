def algo() -> int:
    print("hello, day 8: Treetop Tree House")
    # determine whether there is enough tree cover here to keep a tree house hidden
    # count the number of trees that are visible from outside the grid
    #   example: With 16 trees visible on the edge and another 5 visible in the interior,
    #   a total of 21 trees are visible in this arrangement.

    lines = open("day8_input.txt").readlines()
    grid = [line.strip() for line in lines]

    how_many_visible = 0
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if (x == 0) or (y == 0) or (x == len(grid) - 1) or (y == len(lines) - 1):
                how_many_visible += 1
            else:
                # Get the height of the current tree
                curr_tree = int(grid[x][y])
                print(f'analyzing [{x}][{y}]:{curr_tree}')

                # is it visible from the left?
                visible_left = True
                # range(start, stop, step)
                for k in range(y - 1, -1, -1):
                    # print(f'comparing curr {curr_tree} to left {int(grid[x][z])}')
                    if int(grid[x][k]) >= curr_tree:
                        # print(f'not visible')
                        visible_left = False
                        break

                # # is it visible from the right?
                visible_right = True
                for k in range(y + 1, len(row)):
                    # print(f'comparing curr {curr_tree} to right {int(grid[x][z])}')
                    if int(grid[x][k]) >= curr_tree:
                        # print(f'not visible')
                        visible_right = False
                        break

                # # is it visible from the top?
                visible_top = True
                for k in range(x - 1, -1, -1):
                    # print(f'comparing curr {curr_tree} to top {int(grid[z][y])}')
                    if int(grid[k][y]) >= curr_tree:
                        visible_top = False
                        break

                # # is it visible from the bottom?
                visible_bottom = True
                for k in range(x + 1, len(grid)):
                    # print(f'comparing curr {curr_tree} to bottom {int(grid[k][y])}')
                    if int(grid[k][y]) >= curr_tree:
                        # print(f'not visible')
                        visible_bottom = False
                        break

                if visible_left or visible_right or visible_top or visible_bottom:
                    how_many_visible += 1

    # how many trees are visible from outside the grid
    return how_many_visible


if __name__ == '__main__':
    print(f'result: {algo()}')
