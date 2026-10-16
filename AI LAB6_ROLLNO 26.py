#Implementation of DFS:
class Graph:
    def __init__(self):
        self.graph = {}

    # Add an edge between two nodes
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        # Add the edge in both directions for an undirected graph
        self.graph[u].append(v)
        self.graph[v].append(u)

    # DFS function
    def DFS(self, start):
        stack = [start]
        visited = [start]
        print("DFS traversal order:")
        while stack:
            node = stack.pop()
            print(node, end=" ")

            for neighbour in reversed(self.graph[node]):
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)
            
# Create graph object
g = Graph()
# Add edges
g.add_edge('1', '2')
g.add_edge('1', '7')
g.add_edge('1', '8')
g.add_edge('2', '3')
g.add_edge('2', '6')
g.add_edge('8', '9')
g.add_edge('8', '12')
g.add_edge('3', '4')
g.add_edge('3', '5')
g.add_edge('9', '10')
g.add_edge('9', '11')

# Start DFS
g.DFS('1')
print()
#Task 1
class Graph:
    def __init__(self):
        self.graph = {}

    # Add an edge between two nodes
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        # Add the edge in both directions for an undirected graph
        self.graph[u].append(v)
        self.graph[v].append(u)

    # DFS function
    def DFS(self, start, target):
        stack = [start]
        visited = [start]
        print("DFS traversal order:")
        while stack:
            node = stack.pop()
            print(node, end=" ")

            if node == target:
                print()
                print("Node", node, "found ...")
                break
            
            # Add children to stack (in reverse to maintain order)
            for neighbour in reversed(self.graph[node]):
                if neighbour not in visited:
                     visited.append(neighbour)
                     stack.append(neighbour)
            
        else:
            print()
            print("Node", target, "not found!")

# Create graph object
g = Graph()
# Add edges
g.add_edge('A', 'B')
g.add_edge('A', 'F')
g.add_edge('A', 'D')
g.add_edge('A', 'E')
g.add_edge('B', 'K')
g.add_edge('B', 'J')
g.add_edge('E', 'C')
g.add_edge('D', 'G')
g.add_edge('E', 'H')
g.add_edge('E', 'I')
g.add_edge('I', 'L')
g.add_edge('K', 'N')
g.add_edge('K', 'M')

# Start DFS
g.DFS('A', 'G')

