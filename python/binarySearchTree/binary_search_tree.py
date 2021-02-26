class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.same = []

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree:
    def __init__(self, tree_data):
        list_lenth=len(tree_data)
        if list_lenth > 0:
            top = TreeNode(tree_data[0])
            for i in range(1, list_lenth):
                new_tree_node = TreeNode(tree_data[i])
                while True:
                    if top > new_tree_node:
                        if top.left is None:
                            top.left = new_tree_node
                            break
                        else:
                            top = top.left
                    elif top < new_tree_node:
                        if top.right is None:
                            top.right = new_tree_node
                            break
                        else:
                            top = top.right
                    # same
                    else:
                        top.same.append(new_tree_node)

        else:
            raise Exception("NO DATA")

        self.tree_data = tree_data

    def data(self):
        pass

    def sorted_data(self):
        pass
