from anytree import Node, RenderTree, PostOrderIter


def create_tree_from(commands) -> Node:
    root: Node = Node('root', size=int(0), type='dir')
    current_dir: Node = root

    all_nodes_by_name = dict()
    all_nodes_by_name['root'] = root

    for cmd_raw in commands:
        cmd = cmd_raw.strip()
        match cmd:
            case '$ cd /':
                current_dir = root
            case '$ ls':
                print("ls")
                # ignore
            case '$ cd ..':
                parent = current_dir.parent
                current_dir = parent
            case _:
                if cmd.startswith('$ cd'):
                    _, _, target_dir_name = cmd.split(' ')
                    target_dir = all_nodes_by_name.get(target_dir_name)
                    current_dir = target_dir
                elif cmd.startswith('dir'):
                    _, dir_name = cmd.split(' ')
                    new_dir = Node(dir_name, parent=current_dir, size=int(0), type='dir')
                    all_nodes_by_name[dir_name] = new_dir
                else:
                    file_size, file_name = cmd.split(' ')
                    new_file = Node(file_name, parent=current_dir, size=int(file_size), type='file')
                    all_nodes_by_name[file_name] = new_file
    return root


def visualize_tree(root: Node):
    print('--------')
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))

    all_directories = PostOrderIter(root, filter_=lambda n: n.__getattribute__('type') == 'dir')
    print([directory.name for directory in all_directories])


def calculate_size_of_each_directory(root: Node):
    print('--------')
    print("let's calculate the size of each directory")
    for dir_node in PostOrderIter(root, filter_=lambda n: n.type == 'dir'):
        total_dir_size = 0
        print(f'children of {dir_node.name} are {dir_node.children}')
        for child in dir_node.children:
            total_dir_size += child.__getattribute__('size')

        dir_node.__setattr__('size', total_dir_size)
        print(f'{dir_node.name}, size={dir_node.size}')


def sum_size_of_small_directories(root: Node):
    print('--- filter dirs with size smaller than 100000')
    result_dirs = PostOrderIter(root, filter_=lambda n: n.__getattribute__('type') == 'dir' and n.__getattribute__(
        'size') <= 100000)
    # print([dire.name for dire in result_dirs])

    result = 0
    for d in result_dirs:
        print(d.name)
        result = result + d.__getattribute__('size')

    return result


def algo() -> int:
    print("hello, day 7: No Space Left On Device")
    commands = open("day7_input.txt").readlines()
    root = create_tree_from(commands)
    visualize_tree(root)
    calculate_size_of_each_directory(root)
    return sum_size_of_small_directories(root)


if __name__ == '__main__':
    print(f'result: {algo()}')
    # 1791292 your answer is too low
