# 283. Move Zeroes




class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                j=j+1
        print("The final array is: ", nums)
        


        
obj = Solution();

l1 = [0,1,0,3,12];

obj.moveZeroes(l1)







