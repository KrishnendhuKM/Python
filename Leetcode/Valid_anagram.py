class Solution(object):
    def isAnagram(self, s, t):
      
        s = s.replace(" ", "").lower()
        t = t.replace(" ", "").lower()
    
        return sorted(s) == sorted(t)

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("rat", "car"))   
        