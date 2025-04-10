class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if  target not in nums or nums == [] or target<nums[0]:
            return [-1,-1]

        for i in nums:
            if(i == target):
                first = nums.index(i)
                break
        count = 0
        for j in (nums[first:]):
            if(j == target):
                count+=1
            else:
                break
        last = count + first
        return [first,last-1]

            
            

        