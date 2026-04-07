class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        indices = {}
        for i in range(size):
            num1 = nums[i]
            rem = target-num1 
            if rem in indices:
                return sorted([i,indices[rem]])
            indices[num1] = i
        return []