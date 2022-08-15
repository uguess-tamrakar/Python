from queue import Queue
from typing import Tuple


class Graph:
    adjacency_list = {}

    def __init__(self, vertices, edges) -> None:
        for vertex in vertices:
            self.addVertex(vertex)

        for edge in edges:
            self.addEdges(edge)

    def addVertex(self, vertex):
        self.adjacency_list[vertex] = []

    def addEdges(self, edge: Tuple):
        if (
            edge[0] in self.adjacency_list.keys()
            and edge[1] in self.adjacency_list.keys()
        ):
            self.adjacency_list[edge[0]].append(edge[1])
            self.adjacency_list[edge[1]].append(edge[0])

    def graphBreadthFirstSearch(self, start):
        visited = []
        queue = []
        if start not in self.adjacency_list.keys():
            return []

        queue.append(start)

        while len(queue) > 0:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
            for adjacent in self.adjacency_list[vertex]:
                if adjacent not in visited:
                    queue.append(adjacent)

        return visited

    def graphShortestPath(self, start, end):
        previous_vertices = {}
        queue = []
        if start and end not in self.adjacency_list.keys():
            return []

        queue.append(start)
        while len(queue) > 0:
            previous_vertex = queue.pop(0)
            for adjacent in self.adjacency_list[previous_vertex]:
                if adjacent not in previous_vertices:
                    previous_vertices[adjacent] = previous_vertex
                    queue.append(adjacent)

        shortest_path = []
        current = end
        while current != start:
            shortest_path.append(current)
            current = previous_vertices[current]
        shortest_path.append(start)
        shortest_path.reverse()
        return shortest_path

    def graphDepthFirstSearch(self, start):
        visited = []
        stack = []
        if start not in self.adjacency_list.keys():
            return []

        stack.append(start)

        while len(stack) > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
            for adjacent in self.adjacency_list[vertex]:
                if adjacent not in visited:
                    stack.append(adjacent)

        return visited
