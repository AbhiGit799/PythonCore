'''

1971. Find if Path Exists in Graph

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.

'''

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = {i:[] for i in range(n)}

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node == destination:
                return True

            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
            return False
        
        return dfs(source)


n=3
edges = [[0,1],[1,2]]
source = 0
destination = 2

obj = Solution()

print(obj.validPath(n,edges,source,destination))



print("\n")

for i in range(1,6):
    print(i)


# Time complexity = O(n+m)

# Space = O(n+m)


'''
Solution
==========

1. What is visited = set()?
=============================
visited = set() creates an empty set in Python.

visited = set()

We use it to store the nodes that we have already visited while traversing a graph.

For example:

visited = set()

visited.add(0)
visited.add(1)

print(visited)

Output:
=======
{0, 1}

Here:
- visited.add(0) marks node 0 as visited.
- visited.add(1) marks node 1 as visited.

To check whether a node has been visited:

if 1 not in visited:
    print("Not visited")
else:
    print("Already visited")

Output: Already visited

Why do we need it in a graph?
******************************
Consider this graph:

The graph contains a cycle: 0 → 1 → 2 → 0.

If DFS visits node 0, then node 1, it can return to node 0 through node 2. Without tracking visited nodes, DFS may repeat this cycle forever.

With visited:

visited = set()

visited.add(0)
visited.add(1)
visited.add(2)

When DFS encounters node 0 again, it checks:

if neighbor not in visited:

Since 0 is already in visited, DFS skips it.

Remember: visited prevents repeatedly exploring the same node.


2. Is graph a kind of dictionary?
=================================
Yes! In our solution, graph is a Python dictionary.

graph = {
    0: [1],
    1: [0, 2],
    2: [1]
}

A dictionary stores data as key-value pairs.

Key (node)	      Value (neighbors)
0	               [1]
1	               [0, 2]
2	               [1]

For Ex: print(graph[1])

Output:  [0, 2]

This means node 1 is connected to nodes 0 and 2.

Notice that each dictionary value is a list containing the neighboring nodes.


3. How do we build this dictionary?
Given:
n = 3
edges = [[0, 1], [1, 2]]

First, we create an empty neighbor list for every node:
graph = {i: [] for i in range(n)}


Result = {0: [], 1: [], 2: []}

Then we add the connections:

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)


Final result:

{
    0: [1],
    1: [0, 2],
    2: [1]
}


The two append() statements add the connection in both directions because this problem uses an undirected graph.

Quick revision
================
- graph → dictionary that stores each node and its neighbors.
- visited = set() → stores nodes already explored.
- visited.add(node) → marks a node as visited.
- graph[node] → retrieves the neighbors of that node.
- neighbor not in visited → checks whether we should explore that neighbor.


One useful distinction: the graph dictionary stores connections; the visited set tracks our progress while searching those connections.


'''


'''
Dry Run
========
Since n = 3, the nodes are 0, 1, and 2

graph = {
    0: [],
    1: [],
    2: []
}

Next, process the edges:

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

First edge: [0, 1]
- u = 0, v = 1
- graph[0].append(1) adds 1 to node 0.
- graph[1].append(0) adds 0 to node 1.


Result:
{0: [1], 1: [0], 2: []}


Second edge: [1, 2]
- u = 1, v = 2
- graph[1].append(2) adds 2 to node 1.
- graph[2].append(1) adds 1 to node 2.


Final graph:
============
{
    0: [1],
    1: [0, 2],
    2: [1]
}


3. Step 2 — Initialize visited

visited = set()

Initially, no nodes have been visited.

visited = set()

Now the code calls:

return dfs(source)

Since source = 0, this means:
dfs(0)


6. Complete dry-run summary
============================
DFS call	Condition node == 2	        Visited after marking	      Result
dfs(0)	      False	                      {0}	                      Calls dfs(1)
dfs(1)	      False	                      {0, 1}	                  Calls dfs(2)
dfs(2)	      True	                      {0, 1}	                  Returns True immediately


'''
