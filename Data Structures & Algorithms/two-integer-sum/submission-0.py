class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            num1 = nums[i]
            for j in range(i+1,size):
                num2 = nums[j]
                if (num1+num2==target):
                    return [i,j]
        return []