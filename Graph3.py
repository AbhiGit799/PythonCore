'''
547. Number of Provinces

There are n cities. Some of them are connected, while some are not. 

If city a is connected directly with city b, and city b is connected directly with city c, 
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities 
and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.


'''


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):

            visited.add(city)

            for neighbour in range(n):

                if isConnected[city][neighbour] == 1 and neighbour not in visited:
                    dfs(neighbour)

        for city in range(n):

            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces



isConnected = [[1,1,0],[1,1,0],[0,0,1]]

obj = Solution()

print(obj.findCircleNum(isConnected))


'''

1. Problem understanding

You are given an n x n matrix called isConnected.
- isConnected[i][j] = 1 means city i and city j are directly connected.
- isConnected[i][j] = 0 means they are not directly connected.
A province is a group of cities that are connected directly or indirectly.

Your task is to count the total number of provinces.

isConnected = [
    [1, 1, 0],  # City 0
    [1, 1, 0],  # City 1
    [0, 0, 1]   # City 2
]

We have three cities: 0, 1, 2.

3. Important concept
A province does NOT require multiple cities.
- {0, 1} → One province.
- {2} → Another province (single city).
Even a city with no connection to another city counts as one province.


'''

'''
Suppose we have:

isConnected = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

Here, no cities are connected to each other.

How many provinces will we have?

Exactly! The answer is 3 provinces.

Because:
- City 0 → Province 1
- City 1 → Province 2
- City 2 → Province 3
Each city is isolated, so each forms its own province.


Every time DFS starts from an unvisited city, we discover a new province.

'''





'''

Understanding of Provision concept
====================================

The diagonal positions are:

Position	Value	     Meaning
[0][0]	     1	      City 0 connected to itself
[1][1]	     1	      City 1 connected to itself
[2][2]	     1	      City 2 connected to itself

These values are always 1 because every city is considered connected to itself.

They do not tell us how many provinces exist.


What should we actually check?
We check whether different cities are connected.

Matrix position	  Value	        Meaning
[0][1]	          1	       City 0 connected to City 1
[0][2]	          0	       City 0 not connected to City 2
[1][2]	          0	       City 1 not connected to City 2

Therefore:

Province - 1
{City 0}  -> <-- {City 1}


Province - 2
{City 2}
Total = 2 Provinces


'''

'''
Question Suppose there are 4 cities:

isConnected = [
    [1,1,0,0],
    [1,1,0,0],
    [0,0,1,1],
    [0,0,1,1]
]

How many provinces are there? 

Ans = 2 provinces

Correct!
There are two groups: {0, 1} and {2, 3}.

'''


















