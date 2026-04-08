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
        sortedStr = sorted(strs, key=lambda x: ''.join(sorted(x)))
        i = 0
        while i<size :
            tempArr = [sortedStr[i]]
            j = i+1
            while j<size and isAnagram(sortedStr[i],sortedStr[j]):
                tempArr.append(sortedStr[j])
                j+=1
            ans.append(tempArr)
            i=j
        return ans