class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        counter = 0
        for i in range(len(nums)):
            if nums[i] < target:
                counter+=1
            else:
                return counter
        return counter