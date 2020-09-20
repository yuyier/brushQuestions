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
            if i < list_len:
                tree.left = TreeNode(list_num[i])
                left_node = tree.left
                list.append(left_node)
                i = i + 1
            else:
                break
            if i < list_len:
                tree.right = TreeNode(list_num[i])
                right_node = tree.right
                list.append(right_node)
                i = i + 1
            else:
                break
        return root

    # def create_tree(self, list_num):
    #     list = []
    #     i = 0
    #     list_len = len(list_num)
    #     if list_len < 0:
    #         return
    #     root = TreeNode(list_num[i])
    #     list.append(root)
    #     i = i + 1
    #     while len(list) > 0:
    #         tree = list.pop()
    #         if i < list_len:
    #             tree.left = TreeNode(list_num[i])
    #             left_node = tree.left
    #             list.append(left_node)
    #             i = i + 1
    #         else:
    #             break
    #         if i < list_len:
    #             tree.right = TreeNode(list_num[i])
    #             right_node = tree.right
    #             list.append(right_node)
    #             i = i + 1
    #         else:
    #             break
    #
    #     return root
