class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def bfs_177(root_177):
    if root_177 is None:
        return

    queue_177 = [root_177]
    result_177 = []

    while len(queue_177) > 0:
        cur_node_177 = queue_177.pop(0)
        result_177.append(cur_node_177.val)

        if cur_node_177.left is not None:
            queue_177.append(cur_node_177.left)

        if cur_node_177.right is not None:
            queue_177.append(cur_node_177.right)

    return result_177

def dfs_177(root_177):
    if root_177 is None:
        return

    stack_177 = [root_177]
    result_177 = []

    while len(stack_177) > 0:
        cur_node_177 = stack_177.pop()
        result_177.append(cur_node_177.val)

        if cur_node_177.right is not None:
            stack_177.append(cur_node_177.right)

        if cur_node_177.left is not None:
            stack_177.append(cur_node_177.left)

    return result_177

root_177 = Node("1")
root_177.left = Node("2")
root_177.right = Node("3")
root_177.left.left = Node("4")
root_177.left.right = Node("5")
root_177.right.left = Node("6")
root_177.right.right = Node("7")

print("Binary Tree BFS:", bfs_177(root_177))
print("Binary Tree DFS:", dfs_177(root_177))