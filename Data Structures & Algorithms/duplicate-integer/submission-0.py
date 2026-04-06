class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        siz = len(nums)
        for i in range(siz):
            firstNum = nums[i]
            for j in range(i+1,siz):
                secondNum = nums[j]
                if firstNum == secondNum :
                    return True
        return False

        