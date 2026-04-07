def isAnagram(s : str , t: str) -> bool :
    if (len(s)!=len(t)):
        return False
    freq = [0] * 26 
    for i in range(len(s)):
        freq[(ord(s[i]) - ord('a'))] += 1
        freq[(ord(t[i]) - ord('a'))] -= 1
    for val in freq :
        if val!=0 :
            return False
    return True

class Solution:
    def groupAnagrams(self,strs: list[str]) -> list[list[str]]:
        size = len(strs)
        if size == 1:
            return [[strs[0]]]
        ans = []
        seen = []
        for i in range(size):
            if strs[i] not in seen :
                tempArr = [strs[i]]
                for j in range(i+1, size):
                    if isAnagram(strs[i], strs[j]):
                        tempArr.append(strs[j])
                        seen.append(strs[j])
                ans.append(tempArr)
        return ans