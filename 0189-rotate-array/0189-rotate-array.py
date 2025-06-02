class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,k):
            length = len(nums)
            temp = nums.pop(length-1)
            nums.insert(0,temp)
        