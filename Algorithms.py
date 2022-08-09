from Solution import Solution
from DataStructures import BinarySearchTree, ListNode, TreeNode

problems = [
    Solution.addTwoNumbers.__name__,
    Solution.containsDuplicate.__name__,
    Solution.sherlockAndAnagrams.__name__,
    Solution.lowestCommonAncestor.__name__,
]
solutions = Solution()

print()
for index, problem in enumerate(problems):
    print(f"{index}. {problem}")
print()

input = input("Pick a problem from above: ")

result = ""
intInput = int(input)
problem = problems[intInput]
match problem:
    case Solution.addTwoNumbers.__name__:
        result = solutions.addTwoNumbers(
            ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))
        )
    case Solution.containsDuplicate.__name__:
        result = solutions.containsDuplicate([1, 2, 3, 1])
    case Solution.sherlockAndAnagrams.__name__:
        result = solutions.sherlockAndAnagrams("kkkk")
    case Solution.lowestCommonAncestor.__name__:
        bst = BinarySearchTree()
        for x in 4, 2, 3, 1, 7, 6:
            bst.create(x)
        result = solutions.lowestCommonAncestor(bst.root, 1, 3)

print(f"The result for {problems[intInput-1]} problem is {result}")
