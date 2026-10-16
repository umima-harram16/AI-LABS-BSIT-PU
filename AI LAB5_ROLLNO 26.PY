#Task 1
class Graph:
    def __init__(self, V):
        self.V = V  #vertex count store karne ke liye
        self.adj = {} # hr vertex ka neihbor list store karne ke liye 

        for i in range(V):
            self.adj[i] = []

    def addEdge(self, v, w):
        self.adj[v].append(w)

    def BFS(self, start):
        visited = [False] * self.V
        queue = [start]
        visited[start] = True

        print("BFS Traversal:")

        while len(queue) > 0:
            s = queue.pop(0)
            print(s, end=" ")

            for neighbor in self.adj[s]:
                if visited[neighbor] == False:
                    visited[neighbor] = True
                    queue.append(neighbor)


g = Graph(5)

g.addEdge(0, 1)
g.addEdge(0, 4)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(4, 3)


g.BFS(2)
# Task 2
class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, v, w):
        if v not in self.graph:
            self.graph[v] = []

        if w not in self.graph:
            self.graph[w] = []

        self.graph[v].append(w)

    def BFS(self, start, goal):
        visited = []
        queue = [start]
        visited.append(start)

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            if node == goal:
                print("\nGoal found!")
                return

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

        print("\nGoal not found!")


g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'F')
g.addEdge('A', 'D')
g.addEdge('A', 'E')

g.addEdge('B', 'K')
g.addEdge('B', 'J')

g.addEdge('D', 'G')

g.addEdge('E', 'C')
g.addEdge('E', 'H')
g.addEdge('E', 'I')

g.addEdge('K', 'N')
g.addEdge('K', 'M')

g.addEdge('I', 'L')

g.BFS('A', 'G')
#Task 3
class PriorityQueue:
    def __init__(self):
        self.pq = []

    def push(self, priority, item):
        self.pq.append((priority, item))

    def pop(self):
        self.pq.sort()
        return self.pq.pop(0)

    def display(self):
        while self.pq:
            priority, item = self.pop()
            print(item, "Priority:", priority)


pq = PriorityQueue()

pq.push(3, "C")
pq.push(1, "A")
pq.push(2, "B")

pq.display()