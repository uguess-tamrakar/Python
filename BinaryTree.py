from collections import deque
import queue
from typing import List, Optional

from DataStructures import TreeNode

class BinaryTree:

    def inorderTraversal(root: Optional[TreeNode]):
        result = []
        binary_tree = BinaryTree()
        binary_tree.__
        binary_tree.__traverseRecursive(root, result, "inorder")
        return result

    def preorderTraversal(root: Optional[TreeNode]):
        result = []
        binary_tree = BinaryTree()
        binary_tree.__traverseRecursive(root, result, "preorder")
        return result

    def postorderTraversal(root: Optional[TreeNode]):
        result = []
        binary_tree = BinaryTree()
        binary_tree.__traverseRecursive(root, result, "postorder")
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

    def bstMinDepth(root: TreeNode):
        if root is None:
            return 0
        queue = []
        queue.append([root, 1])
        while len(queue) > 0:
            current = queue.pop(0)
            currentNode = current[0]
            currentDepth = current[1]
            if currentNode.left is None and currentNode.right is None:
                return currentDepth
            else:
                if currentNode.left is not None:
                    queue.append([currentNode.left, currentDepth + 1])
                if currentNode.right is not None:
                    queue.append([currentNode.right, currentDepth + 1])

    def __traverseRecursive(self, current: TreeNode, values: List[int], ordertype):
        if current:
            match ordertype:
                case "inorder":
                    self.__traverseRecursive(current.left, values, ordertype)
                    values.append(current.val)
                    self.__traverseRecursive(current.right, values, ordertype)
                case "preorder":
                    values.append(current.val)
                    self.__traverseRecursive(current.left, values, ordertype)
                    self.__traverseRecursive(current.right, values, ordertype)
                case "postorder":
                    self.__traverseRecursive(current.left, values, ordertype)
                    self.__traverseRecursive(current.right, values, ordertype)
                    values.append(current.val)