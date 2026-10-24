

grid = [[3,2,1],[1,7,6],[2,7,7]]

for row in grid:
    key = tuple(row)
    print(key)

print("\n")
print("\n")

class Solution:
    def equalPairs(self,grid:list[list[int]])->int:
        n = len(grid)
        count = 0

        for r in range(n):
            for c in range(n):
                column = []

                for i in range(n):
                    column.append(grid[i][c])
                    

                if grid[r] == column:
                    print(f"Grid of r = ",grid[r])
                    print(f"Column = ", column)
                    count += 1

        return count


grid = [[3, 2, 1],
        [1, 7, 6],
        [2, 7, 7]]

obj = Solution()
print(obj.equalPairs(grid))






