
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        def backtrack(start, path, total):

            # Base condition
            if len(path) == k:
                if total == n:
                    result.append(path.copy())
                return
        
            # Try numbers from start to 9
            for num in range(start,10):
                #choose
                path.append(num)
                # Explore
                backtrack(num+1, path, total+num)
                # undo choice
                path.pop()
        backtrack(1, [], 0)

        return result


obj = Solution()
k = 3
n = 7
print(obj.combinationSum3(k, n))



















