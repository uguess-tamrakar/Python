class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def createTree(self, values):
        for x in values:
            self.create(x)

    def create(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            current = self.root

            while val is not None:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = TreeNode(val)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = TreeNode(val)
                        break
                else:
                    break
