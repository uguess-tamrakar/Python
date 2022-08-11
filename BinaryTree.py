from collections import deque
import queue
from typing import List, Optional

from DataStructures import TreeNode

class BinaryTree:

    def inorderTraversal(root: Optional[TreeNode]):
        result = []
        binary_tree = BinaryTree()
        binary_tree.traverseRecursive(root, result, "inorder")
        return result

    def preorderTraversal(root: Optional[TreeNode]):
        result = []
        binary_tree = BinaryTree()
        binary_tree.traverseRecursive(root, result, "preorder")
        return result

    def postorderTraversal(root: Optional[TreeNode]):
        result = []
        binary_tree = BinaryTree()
        binary_tree.traverseRecursive(root, result, "postorder")
        return result

    def levelorderTraversal(root: Optional[TreeNode]):
        result = []
        if root:
            queue = deque([root])
            while queue:
                vals = []
                for _ in range(len(queue)):
                    current = queue.popleft()
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                    vals.append(current.val)
                result.append(vals)
        return result

    def traverseRecursive(self, current: TreeNode, values: List[int], ordertype):
        if current:
            match ordertype:
                case "inorder":
                    self.traverseRecursive(current.left, values, ordertype)
                    values.append(current.val)
                    self.traverseRecursive(current.right, values, ordertype)
                case "preorder":
                    values.append(current.val)
                    self.traverseRecursive(current.left, values, ordertype)
                    self.traverseRecursive(current.right, values, ordertype)
                case "postorder":
                    self.traverseRecursive(current.left, values, ordertype)
                    self.traverseRecursive(current.right, values, ordertype)
                    values.append(current.val)