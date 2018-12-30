#!/usr/local/bin/python3

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_len = 0
        longest_list = []
        for x in s:
            if x in longest_list:
                reset_start = longest_list.index(x) + 1
                del longest_list[:reset_start]

            longest_list.append(x)
            longest_len = max(len(longest_list), longest_len)
        return longest_len

s = "ggububgvfk"
# s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))
