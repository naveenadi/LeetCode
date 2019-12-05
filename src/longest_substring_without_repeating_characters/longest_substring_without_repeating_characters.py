class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sub = ''
        ans = 0
        for _ in s:
            if _ in sub:
                sub = sub[sub.index(_)+1:]
            sub += _
            ans = max(ans, len(sub))
        return ans
        
