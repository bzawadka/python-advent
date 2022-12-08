from anytree import Node, RenderTree, PostOrderIter


def create_tree_from(commands) -> Node:
    root: Node = Node('root', size=int(0), type='dir')
    current_dir: Node = root

    for cmd_raw in commands:
        cmd = cmd_raw.strip()
        match cmd:
            case '$ cd /':
                current_dir = root
            case '$ ls':
                print('ls, ignore')
            case '$ cd ..':
                parent = current_dir.parent
                current_dir = parent
            case _:
                if cmd.startswith('$ cd'):
                    _, _, target_dir_name = cmd.split(' ')

                    selected_child = current_dir
                    for child in current_dir.children:
                        if child.name == target_dir_name:
                            selected_child = child
                            break
                    current_dir = selected_child

                elif cmd.startswith('dir'):
                    _, dir_name = cmd.split(' ')
                    Node(dir_name, parent=current_dir, size=int(0), type='dir')
                else:
                    file_size, file_name = cmd.split(' ')
                    Node(file_name, parent=current_dir, size=int(file_size), type='file')
    return root


def visualize_tree(root: Node):
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))

    print('-------- directories post-order')
    all_directories = PostOrderIter(root, filter_=lambda n: n.__getattribute__('type') == 'dir')
    print([directory.name for directory in all_directories])


def calculate_size_of_each_directory(root: Node):
    print("-------- let's calculate the size of each directory")
    for dir_node in PostOrderIter(root, filter_=lambda n: n.type == 'dir'):
        total_dir_size = 0
        # print(f' children of {dir_node.name} are {dir_node.children}')
        for child in dir_node.children:
            total_dir_size += child.__getattribute__('size')

        dir_node.__setattr__('size', total_dir_size)
        print(f'{dir_node.name}, size={dir_node.size}')


def sizes_of_directories_larger_than(root: Node, size_at_least: int):
    print(f'--- filter dirs with size greater than than {size_at_least}')
    result = set()
    result_dirs = PostOrderIter(root, filter_=lambda n: n.__getattribute__('type') == 'dir' and n.__getattribute__('size') >= size_at_least)
    for d in result_dirs:
        print(f'found directory {d.name}')
        result.add(d.__getattribute__('size'))
    return result


def algo() -> int:
    print("hello, day 7: No Space Left On Device")
    # Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update.
    # What is the total size of that directory?

    total_disk_size = 70000000
    required_space = 30000000

    commands = open("day7_input.txt").readlines()
    root = create_tree_from(commands)
    visualize_tree(root)
    calculate_size_of_each_directory(root)

    unused_space = total_disk_size - root.__getattribute__('size')
    needed_space = required_space - unused_space
    print(f"unused space: {unused_space}")

    #  how much space is required?
    if unused_space < required_space:
        print(f'this is not enough space! we need at least {needed_space} more')

    #  which are directories bigger than that?
    sizes = sizes_of_directories_larger_than(root, needed_space)

    print(f'got {len(sizes)} directories to choose from')
    #  which one is the smallest fitting the requirement?
    return min(sizes)


if __name__ == '__main__':
    print(f'result: {algo()}')
    # 1845346 is the right answer!
