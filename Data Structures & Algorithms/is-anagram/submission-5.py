class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False
        count = [0]*26
        for i in range(len(s)):
            index1 = (ord(s[i])-ord('a'))
            index2 = (ord(t[i])-ord('a'))
            count[index1]+=1
            count[index2]-=1
        for num in count :
            if num!=0 :
                return False
        return True