from Graph import Graph
from Solution import Solution
from DataStructures import BinarySearchTree, ListNode, TreeNode
from Strings import Strings

problems = [
    Solution.addTwoNumbers.__name__,
    Solution.containsDuplicate.__name__,
    Solution.sherlockAndAnagrams.__name__,
    Solution.lowestCommonAncestor.__name__,
    Strings.commonChild.__name__,
    Strings.areBalancedBrackets.__name__,
    Graph.graphDepthFirstSearch.__name__,
    Graph.graphBreadthFirstSearch.__name__,
    Graph.graphShortestPath.__name__,
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
    case Strings.commonChild.__name__:
        result = Strings.commonChild("HARRY", "RR")
    case Strings.areBalancedBrackets.__name__:
        result = Strings.areBalancedBrackets(
            "[]][{]{(({{)[})(}[[))}{}){[{]}{})()[{}]{{]]]){{}){({(}](({[{[{)]{)}}}({[)}}([{{]]({{"
        )
    case Graph.graphDepthFirstSearch.__name__:
        vertices = [0, 1, 2, 3, 4]
        edges = [
            (0, 1),
            (0, 2),
            (0, 3),
            (2, 4),
        ]
        graph = Graph(vertices, edges)
        result = graph.graphDepthFirstSearch(0)
    case Graph.graphBreadthFirstSearch.__name__:
        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        edges = [
            (1, 2),
            (1, 3),
            (2, 4),
            (3, 5),
            (3, 6),
            (4, 7),
            (5, 7),
            (5, 8),
            (5, 6),
            (8, 9),
            (9, 10),
        ]
        graph = Graph(vertices, edges)
        result = graph.graphBreadthFirstSearch(1)
    case Graph.graphShortestPath.__name__:
        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        edges = [
            (1, 2),
            (1, 3),
            (2, 4),
            (3, 5),
            (3, 6),
            (4, 7),
            (5, 7),
            (5, 8),
            (5, 6),
            (8, 9),
            (9, 10),
        ]
        graph = Graph(vertices, edges)
        result = graph.graphShortestPath(2, 3)

print(f"The result for {problems[intInput-1]} problem is {result}")
