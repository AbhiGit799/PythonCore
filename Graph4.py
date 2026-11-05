'''
This is an important concept in Graph DSA because identifying whether a graph is a Tree or a General Graph helps us choose the correct approach.

Let's understand how we identified it in LeetCode 1466.
1. What is a Tree in Graph DSA?
A Tree is a connected graph that has no cycles.

There are two important conditions:
1. Every node must be connected (we can reach every node).
2. There must be no cycle (no circular path).
For an undirected tree, there is also a useful mathematical rule:

E = V - 1

Where E is the number of edges and V is the number of vertices. 
This means that if a graph has V vertices, 
it must have exactly V - 1 edges to be a tree.



2. How did we identify a Tree in LeetCode 1466?
Look at the problem constraints:
- There are n cities.
- There are exactly n - 1 roads.
- It is possible to reach every city from any other city if we ignore road directions.


Let's apply the formula.

n = 6

connections = [
    [0, 1],
    [1, 3],
    [2, 3],
    [4, 0],
    [4, 5]
]


Count the nodes:
0, 1, 2, 3, 4, 5

V = 6

Count the roads: 

[0, 1]
[1, 3]
[2, 3]
[4, 0]
[4, 5]

E = 5

Now apply the formula:

E = V - 1

5 = 6 - 1

Because the problem also guarantees that all cities are connected when ignoring directions, we know this graph is a tree.


3. Why is identifying a Tree important?
The biggest advantage is:

There is exactly one path between any two nodes in a tree.

If we start DFS from city 0, every other city has exactly one route connecting it to city 0.

Therefore:
- We don't need to compare multiple possible paths.
- We don't need shortest-path algorithms.
- We simply check the direction of each road while traversing.
That's why DFS is sufficient for this problem.


4. Important: Remember this for LeetCode
 
Graph type	         Characteristics	             Common approach
Tree	             Connected, no cycles	         DFS / BFS
General graph	     Can contain cycles	             DFS / BFS + visited
Directed graph	     Edges have directions	         DFS / BFS, topological sort
Weighted graph	     Edges have costs	             Dijkstra, Bellman-Ford


Note: These categories can overlap. A tree can also be directed or weighted.


'''

'''
LeetCode 1466 – Reorder Routes to Make All Paths Lead to the City Zero

Let's solve this in Python, step by step, using a beginner-friendly explanation.

1. Understand the problem
You are given:
- n cities numbered from 0 to n-1.
- connections[i] = [a, b] means there is a one-way road from city a to city b.
- You need to change the direction of some roads so that every city can reach city 0.
Return the minimum number of roads that must be reversed..


n = 6

connections = [
    [0, 1],
    [1, 3],
    [2, 3],
    [4, 0],
    [4, 5]
]



We need every city to have a path towards city 0.

Initially:
- 0 -> 1 (wrong direction)
- 1 -> 3 (wrong direction)
- 2 -> 3 (wrong direction)
- 4 -> 0 (correct direction)
- 4 -> 5 (wrong direction)
We need to reverse:
- 0 -> 1 into 1 -> 0
- 1 -> 3 into 3 -> 1
- 4 -> 5 into 5 -> 4
Answer = 3


3. Approach: DFS + Graph
The important observation:

We can start DFS from city 0 and visit every other city.

While visiting a city, we check whether the original road direction is pointing away from city 0.

If it is pointing away, we need to reverse it.
Step 1: Build an undirected adjacency list
Why undirected?

Because we need to visit all cities regardless of the original road direction.

However, we must remember the original direction.

For example:

connections = [[0, 1]]

We store:

graph = {
    0: [(1, 1)],
    1: [(0, 0)]
}

Meaning:
- (1, 1) means the original road is 0 -> 1.
- (0, 0) means the original road is 0 -> 1, but we are looking at it from city 1.
The second value tells us whether we need to reverse the road.


'''


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = set()

        def dfs(city):

            visited.add(city)

            changes = 0

            for neighbor, direction in graph[city]:

                if neighbor not in visited:

                    changes += direction

                    changes += dfs(neighbor)

            return changes

        return dfs(0)


'''
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
'''

































