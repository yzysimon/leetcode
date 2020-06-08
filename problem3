class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:  # s is empty string 
            return 0
        i = 0
        j = 1
        max0 = 1
        while j < len(s): 
            if s[j] in s[i:j] and s[i:j] != '':
                if len(s[i:j]) > max0:
                    max0 = len(s[i:j])
                i += 1                    
            else:
                j += 1
        if len(s[i:j]) > max0:
            max0 = len(s[i:j])
        return max0
