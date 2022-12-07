from collections import deque

from anytree import Node, Walker, RenderTree, PostOrderIter


#
#
def algo() -> int:
    print("hello, day 7: No Space Left On Device")

    commands = open("day7_input.txt").readlines()

    root: Node = Node('root', directory_size=int(0), type='dir')
    current_dir: Node = root

    all_nodes_by_name = dict()
    all_nodes_by_name['root'] = root
    nodes_stack = deque()
    nodes_stack.append(root)
    w = Walker()

    for cmd_raw in commands:
        cmd = cmd_raw.strip()
        match cmd:
            case '$ cd /':
                # print("cd root")
                root = nodes_stack.pop()
                w.walk(root, root)
                current_dir = root
            case '$ ls':
                print("ls")
                # ignore
            case '$ cd ..':
                parent = current_dir.parent
                w.walk(current_dir, parent)
                current_dir = parent
            case _:
                if cmd.startswith('$ cd'):
                    _, _, target_dir_name = cmd.split(' ')
                    # print(f'cd {target_dir_name}')
                    target_dir = all_nodes_by_name.get(target_dir_name)
                    w.walk(current_dir, target_dir)
                    current_dir = target_dir
                elif cmd.startswith('dir'):
                    _, dir_name = cmd.split(' ')
                    # print(f'dir {dir_name}')
                    new_dir = Node(dir_name, parent=current_dir, directory_size=int(0), type='dir')

                    all_nodes_by_name[dir_name] = new_dir
                    nodes_stack.append(new_dir)
                else:
                    file_size, file_name = cmd.split(' ')
                    # print(f' file creation {file_name}')
                    new_file = Node(file_name, parent=current_dir, file_size=int(file_size), type='file')

                    s = new_file.__getattribute__('file_size')
                    t = new_file.__getattribute__('type')
                    # print(f'file size {s} {t}')
                    all_nodes_by_name[file_name] = new_file
                    nodes_stack.append(new_file)

    print('--------')
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))

    all_directories = PostOrderIter(root, filter_=lambda n: n.__getattribute__('type') == 'dir')
    print([directory.name for directory in all_directories])

    print('--------')
    print("let's calculate the size of each directory")
    for dir_node in PostOrderIter(root, filter_=lambda n: n.type == 'dir'):
        total_dir_size = 0
        print(f'children of {dir_node.name} are {dir_node.children}')
        for child in dir_node.children:
            match child.__getattribute__('type'):
                case 'file':
                    total_dir_size += child.__getattribute__('file_size')
                case 'dir':
                    total_dir_size += child.__getattribute__('directory_size')

        dir_node.__setattr__('directory_size', total_dir_size)
        print(f'{dir_node.name}, size={dir_node.directory_size}')

    print('--- filter dirs with size smaller than 100000')
    result_dirs = PostOrderIter(root, filter_=lambda n: n.__getattribute__('type') == 'dir' and n.__getattribute__(
        'directory_size') <= 100000)
    # print([dire.name for dire in result_dirs])

    result = 0
    for d in result_dirs:
        print(d.name)
        result = result + d.__getattribute__('directory_size')

    return result


if __name__ == '__main__':
    print(f'result: {algo()}')
    # 1791292 your answer is too low
