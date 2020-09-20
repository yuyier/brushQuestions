# coding=utf-8

class SumOfLeftLeaves(object):
    def sumOfLeftLeaves(self, root):
        sum = 0
        is_left = False
        sum = self.return_left_sum(root, sum, is_left)
        return sum

    def return_left_sum(self, tree, sum, is_left):
        if tree == None:
            return sum
        if is_left and tree.left==None and tree.right==None:
            sum = sum + tree.val
        else:
            sum = self.return_left_sum(tree.left, sum, True)
            sum = self.return_left_sum(tree.right, sum, False)

        return sum
