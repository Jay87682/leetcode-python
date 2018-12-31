#!/usr/local/bin/python3

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_len = 0
        longest_dic = {}
        pivot_start = 0
        for idx, x in enumerate(s):
            guss_pivot = longest_dic.get(x)
            if guss_pivot != None and guss_pivot >= pivot_start:
                pivot_start = guss_pivot + 1

            longest_dic[x] = idx
            longest_len = max(idx - pivot_start + 1, longest_len)
        return longest_len

s = "ggububgvfk"
# s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))
