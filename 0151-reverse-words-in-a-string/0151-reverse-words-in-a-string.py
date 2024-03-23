class Solution:
    def reverseWords(self, s: str) -> str:
        words= []
        new_words = ""
        words = s.split()
        for i in range(len(words)):
            new_words = new_words + words[len(words)-1-i]+" "
        print(new_words)
        output = new_words[:-1]
        return output
        
        
        