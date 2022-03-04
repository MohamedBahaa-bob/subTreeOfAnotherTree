# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recursiveCheck(root, subroot):
    if not subroot:
        return True
    if not root:
        return False
    if sameTree(root, subroot):
        return True
    return recursiveCheck(root.left, subroot) or recursiveCheck(root.right, subroot)


def sameTree(root, subroot):
    if not root and not subroot:
        return True
    if root and subroot and root.val == subroot.val:
        return sameTree(root.left, subroot.left) and sameTree(root.right, subroot.right)
    return False


class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        return recursiveCheck(root, subRoot)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
