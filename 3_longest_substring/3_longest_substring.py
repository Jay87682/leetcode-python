#!/usr/local/bin/python3

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        end_idx = len(s) - 1
        longest_len = 0
        longest_list = []
        next_longest_list = []
        done = False
        for idx, x in enumerate(s):
            next_longest_list.append(x)
            first_match_idx = next_longest_list.index(x)
            next_longest_len = len(next_longest_list) - 1

            if first_match_idx != next_longest_len or next_longest_len == 0:
                if next_longest_len >= longest_len:
                    longest_len = next_longest_len if next_longest_len != 0 else next_longest_len + 1
                    longest_list = next_longest_list[:longest_len]

                if next_longest_len != 0:
                    del next_longest_list[:first_match_idx+1]
                if idx == end_idx:
                    done = True

        if not done:
            next_longest_len = len(next_longest_list)
            if next_longest_len >= longest_len:
                longest_len = next_longest_len
                longest_list = next_longest_list
        return longest_len

s = "ggububgvfk"
# s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))
