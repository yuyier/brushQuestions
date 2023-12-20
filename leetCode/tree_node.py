class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CreateTree(object):
    def return_tree(self, list_num):
        list = []
        i = 0
        list_len = len(list_num)
        if list_len <= 0:
            return None
        root = TreeNode(list_num[i])
        list.append(root)
        i = i + 1
        while len(list) > 0:
            tree = list.pop(0)
            if tree == None:
                continue
            if i < list_len:
                if list_num[i]:
                    tree.left = TreeNode(list_num[i])
                else:
                    tree.left = None
                list.append(tree.left)
                i = i + 1
            else:
                break
            if i < list_len:
                if list_num[i]:
                    tree.right = TreeNode(list_num[i])
                else:
                    tree.right = None
                list.append(tree.right)
                i = i + 1
            else:
                break
        return root
