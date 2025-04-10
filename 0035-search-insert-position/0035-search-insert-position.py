class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        flag = 0
        for i in nums:
            if i >= target:
                flag = 1
                break
        if flag == 1:
            return nums.index(i)
        else:
            return len(nums)
        