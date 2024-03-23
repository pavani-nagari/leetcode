class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        dif= len(word1)-len(word2)
        i=0
        j=0
        newstr=""
        while i<len(word1) and j<len(word2):
            newstr = newstr + word1[i] + word2[j]
            i=i+1
            j=j+1
        if len(newstr) != len(word1)+ len(word2):
            if dif>0:
                newstr = newstr + word1[i:]
            elif dif<0:
                newstr = newstr + word2[j:]
        return newstr



