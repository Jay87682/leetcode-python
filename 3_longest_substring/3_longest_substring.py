#!/usr/bin/python3

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_len = 0
        longest_list = []
        next_longest_list = []
        finish = False
        for idx, x in enumerate(s):
            if x not in next_longest_list:
                next_longest_list.append(x)
            else:
                next_longest_len = len(next_longest_list)
                if next_longest_len >= longest_len:
                    longest_len = next_longest_len
                    longest_list = next_longest_list
                next_longest_list.append(x)    
                reset_begin = next_longest_list.index(x)+1
                # print('reset_begin : ' + str(reset_begin))
                next_longest_list = next_longest_list[reset_begin:]
                # print(next_longest_list)
                if len(next_longest_list) is 0:
                    next_longest_list.append(x)
                if idx == len(s)-1:
                    finish = True

        if len(next_longest_list) >= longest_len and not finish:
            longest_len = len(next_longest_list)
            longest_list = next_longest_list

        print(longest_list)
        return longest_len

# s = "aabaab!bb"
s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))
