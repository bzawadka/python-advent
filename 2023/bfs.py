class Node:
    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val

    def __repr__(self):
        return str(self.val)

    def insert_node(self, val: int):
        if self.val is None:
            return

        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert_node(val)
        else:  # val > self.val OR val is the same
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert_node(val)

    @staticmethod
    def insert_nodes(vals: list[int], root):
        [root.insert_node(i) for i in vals]

    def bfs(self, root=None):
        if root is None:
            return
        queue = [root]
        visited = []

        while len(queue) > 0:
            cur_node = queue.pop(0)

            if cur_node.left is not None:
                queue.append(cur_node.left)

            if cur_node.right is not None:
                queue.append(cur_node.right)

            visited.append(cur_node.val)
            print(f'[in {cur_node}] queue: {queue}')

        print(f'visited: {visited}')


if __name__ == '__main__':
    print('bfs')
    the_root = Node(4)
    the_root.insert_nodes([2, 1, 3, 6, 5, 7], the_root)
    print(the_root)
    the_root.bfs(root=the_root)
