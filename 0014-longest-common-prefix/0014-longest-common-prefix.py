class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        counter = 0

        while True:
            # Stop if counter exceeds length of first string
            if counter >= len(strs[0]):
                break
            
            current_char = strs[0][counter]
            
            # Check if all strings have the same char at this position
            for s in strs:
                if counter >= len(s) or s[counter] != current_char:
                    return prefix  # stop when mismatch found
            
            prefix += current_char
            counter += 1

        return prefix
