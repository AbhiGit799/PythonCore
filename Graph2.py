'''
841. Keys and Rooms

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, 
denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
return true if you can visit all the rooms, or false otherwise.

 

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

'''


class Solution:
    def canVisitAllRooms(self, rooms):
        visited = set()
        def dfs(room):
            if room in visited:
                return
            visited.add(room)
            for key in rooms[room]:
                dfs(key)

        dfs(0)
        return len(visited) == len(rooms)




# Input: rooms = [[1],[2],[3],[]]
# Output: true

obj = Solution()
rooms = [[1],[2],[3],[]]
print(obj.canVisitAllRooms(rooms))


print("\n")
print("\n")

# Simple Ex
aooms = [[1, 3], [3, 0, 1], [2], [0]]
r = 0
for key in aooms[r]:
    print(key)



'''

This problem is a good example of using DFS (Depth First Search) to visit all reachable nodes in a graph.

1. Understand the problem
You are given a list of rooms.
- You start in Room 0.
- Each room contains some keys.
- A key represents the room number you can unlock.
- You can visit a room only if you have its key.
- Return True if you can visit all rooms; otherwise, return False

rooms = [[1], [2], [3], []]

This means:
Room	Keys available
Room 0	1
Room 1	2
Room 2	3
Room 3	None

Can we visit all rooms?

Yes!

Room 0 → Room 1 → Room 2 → Room 3

Output:True


2. DFS approach
We will use three things:
1. visited = set() – stores rooms we have already visited.
2. dfs(room) – visits the current room.
3. Recursion – follows the keys to other rooms.

dfs(0)
Start DFS from Room 0.

return len(visited) == len(rooms)

Compare:
- Number of visited rooms.
- Total number of rooms.
If both are equal, return True.

Time Complexity = O(V+E)
Space = O(V)

'''



