class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        siz = len(nums)
        if siz == 0 or siz == 1 :
            return False
        freqMap = {}
        for num in nums :
            if num not in freqMap.keys() :
                freqMap[num] = 1
            else :
                freqMap[num]+=1
        for value in freqMap.values():
            if value >1 :
                return True
        return False

        